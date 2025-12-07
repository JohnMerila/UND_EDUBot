import csv
import typing as t
from pathlib import Path

from sensor_msgs.msg import LaserScan

def write_to_csv(scan: LaserScan, output_file: t.Union[Path, str]):
    if isinstance(output_file, str):
        output_file = Path(output_file)
    
    if output_file.suffix == 'csv':
        raise RuntimeError(f"We do not support saving to the file type {output_file}")


    with open(output_file, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            # technically, this should be calculated using max-min, and start at min+step
            for i,range in enumerate(scan.ranges):
                writer.writerow([scan.angle_min + i*scan.angle_increment, range])