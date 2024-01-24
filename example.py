import sys


def main(barcode, timestamp, daystamp, device, roll_data_dir, rqp_v2_dir, tapio_dir, drive_letter):
    print(f"BARCODE: {barcode}")
    print(f"TIMESTAMP: {timestamp}")
    print(f"DAYSTAMP: {daystamp}")
    print(f"DEVICE: {device}")
    print(f"ROLL DATA DIR: {roll_data_dir}")
    print(f"RQP V2 DIR: {rqp_v2_dir}")
    print(f"TAPIO DIR: {tapio_dir}")
    print(f"DRIVE LETTER: {drive_letter}")
    print("---")


if __name__ == "__main__":
    if len(sys.argv) != 9:
        print("Invalid number of arguments.")
        sys.exit(1)

    main(*sys.argv[1:])
