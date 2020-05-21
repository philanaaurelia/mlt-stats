# DO NOT GIVE THIS README OR CODED SOLUTION TO THE STUDENTS

## To run the app locally 
1. Log into AWS Educate, and open a Cloud9 Environment

2. Log into course's heroku account by running the following commands in the terminal
- ```sudo snap install heroku --classic``` (if you haven't installed it already)
- ```heroku login -i``` (username is: cosc-458@morgan.edu; password is: M0rg4n+B34rs)

3. Grab the code from Heroku
- ```git clone https://git.heroku.com/cosc458-proj1-music.git``` 

3. Run the following command to install library dependencies locally
- ```cd cosc458-proj1-music```
- ```pip3 install -r requirements.txt```

4. Run the programm locally in AWS
- ```python app.py```

## If the app is showing errors, you may need to refresh access tokens
1.. Sign into developer account at www.Genius.com (search "developer account genius lyrics"). Username=cosc-456@morgan.edu; password=M0rg4n+B34rs. Refresh API tokens

2. Sign into developer account at www.Twitter.com (search "developer account twitter"). Username=cosc-456@morgan.edu; password=M0rg4n+B34rs. Refresh tokens and keys.

# To view on Heroku
1. Head to https://cosc458-proj1-music.herokuapp.com/
