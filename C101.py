
import dropbox
class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def uploadfile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)

def main():
    accesstoken='sl.BPGdo2tLXMKegmCrQcVw2GD_GgMbObsvIRUFx9GAV-qr-kHhe6q58EYF4HcOqiXSGSWbOBf4yOyJEte3j3bbaoTxG7zR_C1n8KPv7y9mm9U0ytERwjGIeFUJAWdrDDszImwLUIwgg2Yv'
    transferData=TransferData(accesstoken)
    filefrom=input('enter the file path that you want to transfer-')
    fileto=input('enter the full path to upload to dropbox')
    transferData.uploadfile(filefrom,fileto)
    print('Your file has been moved.')

main()