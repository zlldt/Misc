from docx import Document
# import pandas

class Solution:
    def getdocxexcel(self,filename):
        d = Document(filename)
        #总行号
        linenumber = 0
        #取每一个表格
        for t in d.tables:
            #取每一列
            for i,columnelement in enumerate(t.columns):
                if i>0:
                    # 取每一大格
                    linenumber += 1
                    for j,cellelement in enumerate(columnelement.cells):
                        if j>0 and j<4:
                            tempstr = str(linenumber)+'-'+str(j)
                            # print(linenumber,'-',j,cellelement.text)
                            print(tempstr, cellelement.text)


test = Solution()
test.getdocxexcel("D:\\临床路径docx\\胫骨平台骨折.docx")
