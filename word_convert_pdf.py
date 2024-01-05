# import os
# from docx2pdf import convert
# word_path = 'C:\Users\99063\Desktop\4.北京语言大学2022-2023学年校级综合奖学金申请审批表.doc'
# word_to_pdf = 'C:\Users\99063\Desktop\4.北京语言大学2022-2023学年校级综合奖学金申请审批表.pdf'
# # 第一个为word路径，第二个为生成word_to_pdf的pdf路径，不用自己创建，会自动创建，可将docx路径直接复制下来，将后缀docx改为pdf就可以了
# convert(word_path, word_to_pdf)



from win32com import client


# 转换doc为pdf
def doc2pdf(fn):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    # for file in files:
    doc = word.Documents.Open(fn)  # 打开word文件
    doc.SaveAs("{}.pdf".format(fn[:-4]), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
    doc.Close()  # 关闭原来word文件
    word.Quit()


# 转换docx为pdf
def docx2pdf(fn):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    # for file in files:
    doc = word.Documents.Open(fn)  # 打开word文件
    doc.SaveAs("{}.pdf".format(fn[:-5]), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
    doc.Close()  # 关闭原来word文件
    word.Quit()


docx2pdf(r'C:\Users\99063\Desktop\4.北京语言大学2022-2023学年校级综合奖学金申请审批表.doc')
# doc2pdf(r'C:\Users\asuka\Desktop\新建文件夹\2.doc')
