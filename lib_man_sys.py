import datetime
import os
class LMS:
    def __init__(self,list_of_books,library_name):
        self.list_of_books="List_of_books.txt"
        self.library_name=library_name
        self.books_dict={}
        Id=101
        with open(self.list_of_books) as bk:
            content=bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),"lender_name":"","Issue_date":"","Status":"Available"}})
            Id=Id+1
    def display_books(self):
        print("-----------------------List of Books------------------------------")
        print("Books ID","\t","Title")
        print("--------------------------------------------------------------------")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")
    def Issue_books(self):
        books_id=input("Enter books ID:")
        current_date=datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict[books_id]["Status"]=="Available":
            print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
            return self.lend_books()
        elif self.books_dict[books_id]['status']=='Available':
            your_name=input("Enter Your Name:")
            self.books_dict[books_id]['lender_name']=your_name
            self.books_dict[books_id]['lend_date']=current_date
            self.books_dict[books_id]['status']='Already Issued'
            print("Book Issued Successfully!!!\n")
        else:
            print("Book ID Not Found!!!")
            return self.Issue_books()
    def add_books(self):
        new_books=input("Enter books title:")
        if new_books=="":
            return self.add_books()
        elif len(new_books)> 50:
            print("Books title length is too lon!!! Title length should be less then 50 characters")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','lend_date':'', 'status':'Available'}})
                print(f"The books '{new_books}'has been added successfully!!!")
    def return_books(self):
        books_id=input("Enter Books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status']=='Available':
                print("This book is already available in library.Please check book id!!!")
                return self.return_books()
            elif not self.books_dict[books_id]['status']=='Available':
                self.books_dict[books_id]['lender_name']=''
                self.books_dict[books_id]['lend_date']=''
                self.books_dict[books_id]['status']='Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")
if __name__=="__main__":
    try:
        myLMS=LMS("list_of_books.txt","Python's")
        press_key_list={"D":"Display Books","I":"Issue Books","A":"Add Books","R":"Return Books","Q":"Quit"}
        key_press=False
        while not (key_press=="q"):
            print(f"\n-----------Welcome To {myLMS.library_name} Library management System-----------\n")
            for key,value in press_key_list.items():
                print("Press",key,"To",value)
            key_press=input("Press Key:").lower()
            if key_press == "i":
                print("\nCurrent Selection: ISSUE BOOK\n")
                myLMS.Issue_books()
            elif key_press =="a":
                print("\nCurrent Selection: ADD BOOK\n")
                myLMS.add_books()
            elif key_press =="d":
                print("\nCurrent Selection: DISPLAY BOOKS\n")
                myLMS.display_books()
            elif key_press =="r":
                print("\nCurrent Selection: RETURN BOOKS\n")
                myLMS.return_books()
            elif key_press =="q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong.Please check again!!!")
    #l=LMS("List_of_books.txt","Python's Library")
    #print(l.display_books())
#print(LMS("List_of_books.txt","Python's Library"))

