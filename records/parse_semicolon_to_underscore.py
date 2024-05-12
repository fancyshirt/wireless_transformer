import sys, os
import argparse

if os.system("clear") != 0:
    os.system("cls")

parser = argparse.ArgumentParser(description='save torch experience file to npy.')
parser.add_argument('-s', '--source_folder', help='source torch experience file directory.', required=True)
parser.add_argument('-y', help='yes to all', action='store_true')
args = parser.parse_args()


def main():
    folders = os.listdir(args.source_folder)
    
    for folder in folders:
        print('-'*20)
        full_folder_path = f"{args.source_folder}{folder}"
        print(f"{full_folder_path = }")
        filenames = os.listdir(full_folder_path)
        for filename in filenames:
            # print(f"{filename = }")
            new_filename = filename.replace(":", "_")
            # print(f"{new_filename = }")
            # print('.'*10)
            old_full_filename = f"{full_folder_path}/{filename}"
            new_full_filename = f"{full_folder_path}/{new_filename}"
            print(f"{old_full_filename = }")
            print(f"{new_full_filename = }")
            # os.rename()
            break

    pass


if __name__ == '__main__':
    main()


