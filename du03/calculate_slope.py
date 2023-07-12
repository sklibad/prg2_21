import argparse
import numpy as np
import rasterio
from rasterio.windows import Window

def calculate_slope(terrain_raster: np.ndarray):
    # Calculates slope using gradients

    x_gradient = np.gradient(terrain_raster, axis = 1)
    y_gradient = np.gradient(terrain_raster, axis = 0)
    slope_radians = np.arctan(np.sqrt(x_gradient**2 + y_gradient**2))
    slope_degrees = np.degrees(slope_radians)
    return slope_degrees

def get_intersection(terrain_raster: str, surface_raster: str):
    # Calculates intersection between raster extents

    with rasterio.open(terrain_raster) as terrain:
        with rasterio.open(surface_raster) as surface:
            terrain_extent = terrain.bounds
            surface_extent = surface.bounds

            # Calculate the intersection extent
            intersection_min_x = max(terrain_extent[0], surface_extent[0])
            intersection_min_y = max(terrain_extent[1], surface_extent[1])
            intersection_max_x = min(terrain_extent[2], surface_extent[2])
            intersection_max_y = min(terrain_extent[3], surface_extent[3])

            # Check if there is a valid intersection
            if intersection_min_x < intersection_max_x and intersection_min_y < intersection_max_y:
                intersection = (intersection_min_x, intersection_min_y, intersection_max_x, intersection_max_y)
            else:
                raise ValueError("No intersection found between the input rasters.")
            
            # Convert the spatial coordinates to pixel coordinates
            transform = terrain.transform
            pixel_coords = rasterio.transform.rowcol(transform, [intersection[0], intersection[2]], [intersection[1], intersection[3]])
            first_row = pixel_coords[0][1]
            first_column = pixel_coords[1][0]
            height = abs(pixel_coords[0][0] - pixel_coords[0][1])
            width = abs(pixel_coords[1][1] - pixel_coords[1][0])        

    return first_row, first_column, height, width

def main():
    # Limit difference between rasters
    limit = 0.1

    # Output file names
    mask_output = "mask.tiff"
    slopes_output = "slopes.tiff"

    # Size of computational window
    step = 512

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--terrain", required = True)
    parser.add_argument("--surface", required = True)
    args = parser.parse_args()
    
    # Get intersection of raster extents
    first_row, first_column, height, width = get_intersection(args.terrain, args.surface)
    
    # Open surface elevation raster
    with rasterio.open(args.surface) as surface:

        # Read raster metadata
        kwargs = surface.meta
        kwargs.update(dtype=rasterio.float32, count=1, compress='lzw')

        # Open terrain elevation raster
        with rasterio.open(args.terrain) as terrain:

            # Open output rasters in write mode
            with rasterio.open(slopes_output, 'w', **kwargs) as slopes:
                with rasterio.open(mask_output, 'w', **kwargs) as mask:

                    # Iterate over number of rows given by step constant in total range of raster height
                    for row in range(0, height, step):

                        # If row+step exceeds height
                        if row + step > height:                           
                            # Decrease number of rows, so it fits into raster bounds
                            row_step = height - row
                        else:
                            # Otherwise maintain the current number of rows
                            row_step = step

                        # Iterate over number of columns given by step constant in total range of raster width
                        for col in range(0, width, step):

                            # If col+step exceeds width
                            if col + step > width:
                                # Decrease number of columns, so it fits into raster bounds
                                col_step = width - col              
                            else:
                                # Otherwise maintain the current number of columns
                                col_step = step

                            # Read rasters in current window
                            terrain_win = Window(col, row + first_row, col_step, row_step)
                            surface_win = Window(col, row, col_step, row_step)
                            terrain_window = terrain.read(1, window = terrain_win).astype(float)
                            surface_window = surface.read(1, window = surface_win).astype(float)

                            # Find undeveloped areas by comparing rasters
                            difference = np.abs(terrain_window - surface_window)
                            mask_window = np.where(difference <= limit, 1, 0)

                            # Calculate slope
                            slopes_window = calculate_slope(terrain_window)

                            # Mask slope values
                            slopes_window = slopes_window*mask_window

                            # Write raster window into rasters
                            mask.write(mask_window.astype(rasterio.float32), indexes = 1, window = surface_win)
                            slopes.write(slopes_window.astype(rasterio.float32), indexes = 1, window = surface_win)

if __name__ == "__main__":
    main()
