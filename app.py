from requests import get
from bs4 import BeautifulSoup
from flask import Flask,render_template,request,redirect,url_for


#web scraping the content from imdb website using BeautifulSoup
url='https://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1'


response=get(url)
 
html_soup=BeautifulSoup(response.text,'html.parser')

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')


#creating seaparate dictionary for movies
actionMovies={}
adventureMovies={}
fantasyMovies={}
science_fictionMovies={}
comedyMovies={}
biographyMovies={}
dramaMovies={} 
musicalMovies={}
horrorMovies={}
mysteryMovies={}
thrillerMovies={}
romanceMovies={}
crimeMovies={}

#searching for specific Genre and movieRating of movie and appending them in particular dictionaries
for movie in movie_containers:
     movieGenre=movie.p.find('span',class_='genre').text.strip()
     movieGenre=str(movieGenre)
     movieRating=movie.strong.text
     movieGenre=list(movieGenre.split(', '))
     for Genre in movieGenre:
          if Genre=="Action" or Genre=="\nAction":
               actionMovies.update({movieRating:movie})

          if Genre=="Adventure" or Genre=="\nAdventure":
               adventureMovies.update({movieRating:movie})
               
          if Genre=="Fantasy" or Genre=="\nFantasy":
               fantasyMovies.update({movieRating:movie})
               
          if Genre=="Sci-Fi" or Genre=="\nSci-Fi":
               science_fictionMovies.update({movieRating:movie})

          if Genre=="Comedy" or Genre=="\nComedy":
               comedyMovies.update({movieRating:movie})
                                

          if Genre=="Biography" or Genre=="\nBiography":
                biographyMovies.update({movieRating:movie})
                   
          if Genre=="Drama" or Genre=="\nDrama":
                dramaMovies.update({movieRating:movie})

          if Genre=="Musical" or Genre=="\nMusical" or Genre=="\nMusic" or Genre=="Music":
                musicalMovies.update({movieRating:movie})
               
          if Genre=="Horror" or Genre=="\nHorror":
                horrorMovies.update({movieRating:movie})
               

          if Genre=="Mystery" or Genre=="\nMystery":
                mysteryMovies.update({movieRating:movie})
               
          if Genre=="Thriller" or Genre=="\nThriller":
                thrillerMovies.update({movieRating:movie})
               
          if Genre=="Romance" or Genre=="\nRomance":
                romanceMovies.update({movieRating:movie})
               
          if Genre=="Crime" or Genre=="\nCrime":
               crimeMovies.update({movieRating:movie})


#sorting the movies according to top movieRatings
actionMoviesSorted=actionMovies.keys()
actionMoviesSorted.sort(reverse=True)

adventureMoviesSorted=adventureMovies.keys()
adventureMoviesSorted.sort(reverse=True)


fantasyMoviesSorted=fantasyMovies.keys()
fantasyMoviesSorted.sort(reverse=True)

science_fictionMoviesSorted=science_fictionMovies.keys()
science_fictionMoviesSorted.sort(reverse=True)

comedyMoviesSorted=comedyMovies.keys()
comedyMoviesSorted.sort(reverse=True)

biographyMoviesSorted=biographyMovies.keys()
biographyMoviesSorted.sort(reverse=True)
  
dramaMoviesSorted=dramaMovies.keys()
dramaMoviesSorted.sort(reverse=True)

musicalMoviesSorted=musicalMovies.keys()
musicalMoviesSorted.sort(reverse=True)

horrorMoviesSorted=horrorMovies.keys()
horrorMoviesSorted.sort(reverse=True)
     
mysteryMoviesSorted=mysteryMovies.keys()
mysteryMoviesSorted.sort(reverse=True)

thrillerMoviesSorted=thrillerMovies.keys()
thrillerMoviesSorted.sort(reverse=True)

romanceMoviesSorted=romanceMovies.keys()
romanceMoviesSorted.sort(reverse=True)

crimeMoviesSorted=crimeMovies.keys()
crimeMoviesSorted.sort(reverse=True)

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():                    
     #macting the search page
     if request.method=="POST":
           searchKey=request.form['search']
           if(searchKey=="Action"):
                return redirect(url_for('action_movies'))

           if(searchKey=="Adventure"):
                return redirect(url_for('adventure_movies'))

           if(searchKey=="Fantasy"):
                return redirect(url_for('fantasy_movies'))

           if(searchKey=="Science_Fiction"):
                return redirect(url_for('science_fiction_movies'))

           if(searchKey=="Comedy"):
                return redirect(url_for('comedy_movies'))

           if(searchKey=="Biography"):
                return redirect(url_for('biography_movies'))

           if(searchKey=="Drama"):
                return redirect(url_for('drama_movies'))
   
           if(searchKey=="Musical"):
                return redirect(url_for('musical_movies'))

           if(searchKey=="Horror"):
                return redirect(url_for('horror_movies'))

           if(searchKey=="Mystery"):
                return redirect(url_for('mystery_movies'))
 
           if(searchKey=="Thriller"):
                return redirect(url_for('thriller_movies'))

           if(searchKey=="Romance"):
                return redirect(url_for('romance_movies'))

           if(searchKey=="Crime"):
                return redirect(url_for('crime_movies'))
      
     return render_template('index.html')

@app.route("/action_movies")
def action_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in actionMoviesSorted[:5]:
          movieNames.append(actionMovies[key].h3.a.text)
          movieReleaseYear.append(actionMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(actionMovies[key].strong.text))
          v=actionMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=actionMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=actionMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(actionMovies[key].a.img['src'])
     return render_template('action.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)


@app.route("/adventure_movies")
def adventure_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in adventureMoviesSorted[:5]:
          movieNames.append(adventureMovies[key].h3.a.text)
          movieReleaseYear.append(adventureMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(adventureMovies[key].strong.text))
          v=adventureMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=adventureMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=adventureMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(adventureMovies[key].a.img['src'])
     return render_template('adventure.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)


@app.route("/fantasy_movies")
def fantasy_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in fantasyMoviesSorted[:5]:
          movieNames.append(fantasyMovies[key].h3.a.text)
          movieReleaseYear.append(fantasyMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(fantasyMovies[key].strong.text))
          v=fantasyMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=fantasyMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=fantasyMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(fantasyMovies[key].a.img['src'])
     return render_template('fantasy.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)


@app.route("/science_fiction_movies")
def science_fiction_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in science_fictionMoviesSorted[:5]:
          movieNames.append(science_fictionMovies[key].h3.a.text)
          movieReleaseYear.append(science_fictionMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(science_fictionMovies[key].strong.text))
          v=science_fictionMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=science_fictionMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=science_fictionMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(science_fictionMovies[key].a.img['src'])
     return render_template('science_fiction.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
        

@app.route("/comedy_movies")
def comedy_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in comedyMoviesSorted[:5]:
          movieNames.append(comedyMovies[key].h3.a.text)
          movieReleaseYear.append(comedyMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(comedyMovies[key].strong.text))
          v=comedyMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=comedyMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=comedyMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(comedyMovies[key].a.img['src'])
     return render_template('comedy.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
        

@app.route("/biography_movies")
def biography_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in biographyMoviesSorted[:5]:
          movieNames.append(biographyMovies[key].h3.a.text)
          movieReleaseYear.append(biographyMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(biographyMovies[key].strong.text))
          v=biographyMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=biographyMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=biographyMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(biographyMovies[key].a.img['src'])
     return render_template('biography.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
        
@app.route("/drama_movies")
def drama_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in dramaMoviesSorted[:5]:
          movieNames.append(dramaMovies[key].h3.a.text)
          movieReleaseYear.append(dramaMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(dramaMovies[key].strong.text))
          v=dramaMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=dramaMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=dramaMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(dramaMovies[key].a.img['src'])
     return render_template('drama.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
        

@app.route("/musical_movies")
def musical_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in musicalMoviesSorted[:5]:
          movieNames.append(musicalMovies[key].h3.a.text)
          movieReleaseYear.append(musicalMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(musicalMovies[key].strong.text))
          v=musicalMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=musicalMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=musicalMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(musicalMovies[key].a.img['src'])
     return render_template('musical.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
        

@app.route("/horror_movies")
def horror_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in horrorMoviesSorted[:5]:
          movieNames.append(horrorMovies[key].h3.a.text)
          movieReleaseYear.append(horrorMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(horrorMovies[key].strong.text))
          v=horrorMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=horrorMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=horrorMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(horrorMovies[key].a.img['src'])
     return render_template('horror.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
        
@app.route("/mystery_movies")
def mystery_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in mysteryMoviesSorted[:5]:
          movieNames.append(mysteryMovies[key].h3.a.text)
          movieReleaseYear.append(mysteryMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(mysteryMovies[key].strong.text))
          v=mysteryMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=mysteryMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=mysteryMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(mysteryMovies[key].a.img['src'])
     return render_template('mystery.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
        
                
@app.route("/thriller_movies")
def thriller_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in thrillerMoviesSorted[:5]:
          movieNames.append(thrillerMovies[key].h3.a.text)
          movieReleaseYear.append(thrillerMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(thrillerMovies[key].strong.text))
          v=thrillerMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=thrillerMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=thrillerMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(thrillerMovies[key].a.img['src'])
     return render_template('thriller.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
                
@app.route("/romance_movies")
def romance_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in romanceMoviesSorted[:5]:
          movieNames.append(romanceMovies[key].h3.a.text)
          movieReleaseYear.append(romanceMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(romanceMovies[key].strong.text))
          v=romanceMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=romanceMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=romanceMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(romanceMovies[key].a.img['src'])
     return render_template('romance.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
                
@app.route("/crime_movies")
def crime_movies():
     movieNames=[]
     movieReleaseYear=[]
     movieRatings=[]
     movieVotes=[]
     movieDiscription=[]
     movieActors=[]
     movieImages=[]
     for key in crimeMoviesSorted[:5]:
          movieNames.append(crimeMovies[key].h3.a.text)
          movieReleaseYear.append(crimeMovies[key].h3.find('span', class_ = 'lister-item-year text-muted unbold').text)
          movieRatings.append(float(crimeMovies[key].strong.text))
          v=crimeMovies[key].find('span', attrs = {'name':'nv'})
          movieVotes.append(int(v['data-value']))
          m=crimeMovies[key].find("p").findNext("p").get_text()
          movieDiscription.append(m)     
          ma=crimeMovies[key].find("p").findNext("p").findNext("p").get_text()
          movieActors.append(ma) 
          movieImages.append(crimeMovies[key].a.img['src'])
     return render_template('crime.html',mN=movieNames,mRY=movieReleaseYear,mR=movieRatings,mV=movieVotes,mD=movieDiscription,mA=movieActors,mI=movieImages)
                


if __name__=="__main__":

     app.run(debug=True)











       
     







