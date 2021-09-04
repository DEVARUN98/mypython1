overriding
same method name,same num of arguments


class Books:
    def printv(self,bk_name,pages):
        self.bk_name=bk_name
        self.pages=pages
        print(self.bk_name,self.pages)
class Publication(Books):
    def printv(self,copies,pblctn_mnth):
        self.copies=copies
        self.pblctn_mnth=pblctn_mnth
        print(self.copies,self.pblctn_mnth)
pb=Publication()
pb.printv(100,'January')