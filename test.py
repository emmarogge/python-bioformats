from bioformats import formatreader as fr

if __name__ == "__main__":
    ImageReader = fr.make_image_reader_class()
    reader = ImageReader()
    reader.download("gs://emmarogge-05-13-2022-cellprofiler-resources-bucket-test/AS_09125_050116030001_D03f00d0.tif")
    print("Downloaded image.")
