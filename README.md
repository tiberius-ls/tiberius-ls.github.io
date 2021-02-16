# tiberius-ls.github.io



# run the app

### run the following command from the MAIN APP folder 
##### Activate the env
`cd bb\Scripts && activate` 
 ##### return to the project folder 
`cd .. && cd ..`

 ##### create a .env file with the following variables  in the  `voent` folder
`STATIC_ACTION=True`

 ##### run migrations
`python manage.py makemigrations`
`python manage.py migrate  `
`python manage.py runserver`
