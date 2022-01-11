from subprocess import check_call
import sys, fnmatch, os
from os import path as oSpath
from PIL import Image
import logging
from info import start
from PIL.ExifTags import TAGS, GPSTAGS


def initLogger(name):
    """
    Keep things as simple as possible for the moment
    """
    path = os.path.dirname(os.path.realpath(__file__))
    logfile = f"{path}/{name}.log"

    logging.basicConfig(
        format="%(asctime)s\t%(levelname)s\t%(message)s",
        filemode="a",
        filename=logfile,
        level=logging.INFO,
    )


def check_GoPro(fcwd):
    """
    check the existance of the gopro.exe in the same folder of this script
    """
    if not (oSpath.isfile(os.path.join(fcwd, "FusionStudio_x64.exe.lnk"))):
        logging.error("The script is running in the wrog folder")
        sys.exit()
    return


def get_num_pixels(path):
    """
    get number of pixel of an image
    """
    width, height = Image.open(path).size
    return width * height


def mk_output_folder(path, folder):
    """
    if a folder (with name "folder") does not exist, it is created
    """
    if not oSpath.exists(oSpath.join(path, folder)):
        os.makedirs(oSpath.join(path, folder))
    return


def get_exif(path):
    """
    from
    https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3
    """
    image = Image.open(path)
    image.verify()
    return image._getexif()


def get_geotagging(exif, filepath):
    """
    from
    https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3
    filepath needs only for logging
    """
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == "GPSInfo":
            if idx not in exif:
                logging.error(f"No EXIF geotagging found for {filepath}")
                return
                # raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging


def use_GoPro(froot, fname, front, output):
    """
    launch the FusionStudio_x64.exe from the cmd
    """

    command_list = [
        "cmd",
        "/c",
        ".\FusionStudio_x64.exe.lnk",
        "--back",
        oSpath.join(froot, fname),
        "--front",
        front,
        "--output",
        output,
        "--projection",
        "0",
        "--pc",
        "0",
        "--width",
        "5760",
    ]

    logging.info(command_list)
    check_call(command_list)

    return


def main():

    LOGFILENAME = os.path.basename(__file__).split(".")[0]
    initLogger(LOGFILENAME)

    cwd = os.getcwd()

    check_GoPro(cwd)

    # pattern = "GB*.jpg"
    pattern = "GB01000*.jpg"

    datiInput = oSpath.join(start)

    # check if output folder exists and create it
    mk_output_folder(datiInput, "output")

    outputFolder = oSpath.join(datiInput, "output")

    for root, dirs, files in os.walk(datiInput, topdown=False):
        for name in files:
            if fnmatch.fnmatch(name, pattern):

                # GB010001.jpg --> 010001
                outputStringName = name[2:-4]

                # path of the folder containing FRONT and BACK
                folderNamePath = oSpath.dirname(root)

                # name of the folder containing FRONT and BACK
                foldername = oSpath.basename(folderNamePath)

                # name of the FRONT folder (FRNT)
                nameFront = oSpath.basename(root).split("BACK")[0] + "FRNT"

                frontFolderFile = oSpath.join(
                    folderNamePath, nameFront, f"GF{outputStringName}.jpg"
                )

                mk_output_folder(outputFolder, foldername)

                # output file: stich01...jpg
                outputFolderFile = oSpath.join(
                    outputFolder, foldername, f"stich{outputStringName}.jpg"
                )

                if (oSpath.isfile(outputFolderFile)) and (get_num_pixels(outputFolderFile) == 16588800):

                    exif = get_exif(outputFolderFile)
                    # dict of 8 elements
                    geotags = get_geotagging(exif, outputFolderFile)

                    logging.info(
                        f"{outputFolderFile} already exists: pixel dimension {get_num_pixels(outputFolderFile)}, geoloc {geotags}"
                    )
                    continue

                use_GoPro(root, name, frontFolderFile, outputFolderFile)


if __name__ == "__main__":
    main()
