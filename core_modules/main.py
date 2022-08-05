# to create requirements.txt use terminal "pipreqs --encoding=utf-8 ./ --force"

import settings
import helper
import colortest
#helper -> colortest
import pandas as pd








class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class testing_area:
    # testing face data class 
    def __init__(self):
        self.data_dir = settings.data_dir
        if not helper.file_validation(self.data_dir):
            print("now unzipping tar")
            try:
                helper.unzip_tar(settings.tardir)
            except Exception as e:
                print(f"something went wrong in {e}")
                # raise CustomException("\n\n \"extraction has\"\n")
    def get_all_rgb_data(self):
        pictures = helper.listdirs4(self.data_dir)
        data = []
        directory = []
        for pic in pictures:
            # print(pic)
            # colortest.get_rgb2()
            try:        
                data.append(colortest.get_rgb2(colortest.crop_face(pic)))
                directory.append(pic)
            except Exception as e:
                print(e)
                pass
        # helper.write_as_file("face_rgb_data",data)
        return data,directory
                
    # def create_df(self,d,dr):
    #     df1 = pd.Series(d)
    #     df1.index = (dr)
    #     df1.index.name = "picture directory"
    #     return df1
    
    def create_df(self,d,dr):
        # d for data, dr for directory
        df = pd.DataFrame(d)            
        df.columns = ["R","G","B"]
        df.index = dr
        return df        
        

    def test(self):
        print(self.data_dir)
        print("gg")



a = testing_area()
if __name__ == '__main__':
    rgbdata = a.get_all_rgb_data()
    # try:
        # df1 = a.create_df(rgbdata[0],rgbdata[1])
        # print("df1 done")
    # except Exception as e:
        # print(e)
        
    # print(df1)


    # df1.to_csv("df1.csv", mode='w')



