import os
from PIL import Image
maxwidth = 600

class Solution:
    def resizedirfiles(self, dirname):
        destdir = 'E:\\resize\\'
        print(sum([len(files) for root, dirs, files in os.walk(dirname)]))
        count = 0
        for root, dirs, files in os.walk(dirname):
            for file in files:
                print(root + '\\' + file)
                if file.endswith('.jpg'):
                    im = Image.open(root + '\\' + file)
                    w, h = im.size
                    if w > maxwidth:
                        new_h = maxwidth*h/w
                        new_w = maxwidth
                        output = im.resize((int(new_w), int(new_h)), Image.ANTIALIAS)
                        output.save(destdir+file, 'jpeg')
                    count += 1
        print('修改大小的图片数量：', count)
        return


test = Solution()
test.resizedirfiles('E:\\1')
