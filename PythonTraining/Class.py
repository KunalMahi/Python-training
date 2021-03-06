class User:
    def SetUserName(self,userName):
        self._UserName=userName
    def GetUserName(self):
        return self._UserName

def main():
    u1=User()
    u1.SetUserName("Hussien")
    print(u1.GetUserName())
    u2=User()
    u2.SetUserName("Kunal")
    print(u2.GetUserName())

if __name__ == '__main__':main()
