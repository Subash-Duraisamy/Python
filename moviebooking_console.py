import os;
import json;

Movie_PATH="movies.json";
class MovieSystem:
    def __init__(self):
        self.movies = self.import_movies();
    def import_movies(self):
        if os.path.exists(Movie_PATH):
            with open('movies.json','r') as file :
                return json.load(file);
        return [];
    def Add_Movies(self,title,seats):
        self.movies.append({"title":title,"seats":seats});
        self.save();
    def save(self):
        with open('movies.json','w') as file:
            json.dump(self.movies,file,indent=4);
    def Remove_Movies(self,title):
        self.movies=[movie for movie in self.movies if movie["title"]!=title];
        self.save();

    def View_Movies(self):
        if not self.movies:
            return "No movies found";
        else:
            for idx,movie in enumerate(self.movies,start=1):
             print(idx,movie["title"],movie["seats"]);

    def Book_Movies(self,title):
        for movie in self.movies:
            if movie["title"]==title:
                if movie["seats"]>0:
                    movie["seats"]-=1;
                    self.save();
                    print("Seat Booked for the movie");
                    return
                else:
                    print("Movie is already fully booked");
                    return;

        return "Moview not found";





def Admin_Access(object) :
    print("\nAdmin Page :");
    print("\n1 - Adding Movies");
    print("\n2 - Removing Movies");
    print("\n3 - Viewing all Movies");
    Admin_choice=int(input("\nEnter your choice : "));
    if Admin_choice==1 :
        title = input("\nEnter the movie title: ");
        seats = int(input("\nEnter the number of seats: "));
        object.Add_Movies(title,seats);
    elif Admin_choice==2 :
        title= input("\nEnter the movie title: ");
        object.Remove_Movies(title);
    elif Admin_choice==3 :
        object.View_Movies()
    else:
        print("Back to main page");

def User_Access(object) :

    print("\n1 - Viewing all Movies");
    print("\n2 - Booking Movies");
    print("\n3 - Back to main page");
    User_choice = int(input("\nEnter your choice : "));
    if User_choice==1 :
        object.View_Movies()
    elif User_choice==2 :
        object.Book_Movies(input("\nEnter the movie title: "))
    else:
        print("Back to main page");


if __name__=="__main__":
    Object = MovieSystem();
    print("\n#MOVIE Booking Console Application");

    print("\n1 . for Admin Access");
    print("\n2 . for USer Access");
    print("\n3 . Quiting");

    main_choice = int(input("Type Your Choice : "));
    if main_choice == 1:
        Admin_Access(Object)
    elif main_choice == 2:
        User_Access(Object)
    else :
        print("Thank you for choosing this Booking Application");
        exit();



