# BatiBot-The-Discord-Bot

The Discord Bot that will replace my existence and automate most of my stuff.
Don't Question The Name, I called it that to annoy a certain someone.

# What does this bot even do ? 
This discord bot aims to automate some tasks, that I think most people struggle with in Discord Servers.
As of now one of the major features that I am trying to implement is making the Discord Bot display daily,
upcoming CP (Competitive Programming) Contests around the globe, with the use of the CList API.
# So how do I use this bot of yours?
Install all needed packages by running:
```pip install -r requirements/requirements.txt```

Note: You can also use virtual environment in Python if you prefer so. I reccomend doing so, to properly manage packages in python.
```python3 -m venv myenv```

Run the bot by using the following command:
```python3 app/bot.py```


### Git Commands, Tips, Tricks and How to Contribute To this Project
### Legend and Explanation of Each Command

| Commands                                     | Command's Use and Explanation                                         |
|----------------------------------------------|-----------------------------------------------------------------------|
| git checkout                                 | Let's you go to another branch located in your local machine.         |           
| git clone                                    | gives you a copy of the repository.                                   |
| git status                                   | displays the status of the current git action/process you are doing.  |
| git add                                      | "Stage" or choose the changes what would be applied to the repository.|
| git commit                                   |  Further Prepares the changes to be submitted.                        |    
| git push -u origin {YourName}-Branch         | Finally, apply all the changes                                        |           


| Options                             | Option's Use and Explanation                                                     |
|-------------------------------------|----------------------------------------------------------------------------------|
| --all                               | It specifies that it adds all changes, used in conjunction with git add.         |
| -m "Write here what you changed"    | adds a small message, specifying what you changed.                               |
| -u                                  | I honestly don't know I just use it. Please refer to the documentation.          |
| origin                              | This specifies to change your copy in Github.                                    |
| -b                                  | when the branch does not exist, make one. Used in conjunction with git checkout. |
| {YourName}-Branch                   | name of the branch you are pertaining to in the command.                         |


# Step 0 : What is Github?  ( Optional)

#### I reccomend you watch this video to get a basic gist of how github works and the process we are conducting.
Link : https://www.youtube.com/watch?v=w3jLJU7DT5E

# Step 1 : Install Git in your machine

Please install Git in your machine, for you to be able to use it in your respective command line/terminals. (Also known as cmd in windows, and Terminals in Unix Machines)

Use this link as reference.
Link: https://www.atlassian.com/git/tutorials/install-git

# Step 2 :  Fork this Repository
There is a clickable button in your top-right, click it and it will give a copy of my entire repository to you.


# Step 3 : Submitting my work

-Go to the repository/directory/folder where this copy of the repository is saved.
- Type the command : ```git checkout -b {YourName}-Branch```
- Type the command : ```git status```
 * Check the files you have modified or changed.
 - Type the command : ```git add --all```
- Type the command : ```git commit -m "Write here what you changed".```
- Type the command : ```git push -u origin {YourName}-Branch```
- Enter your github credentials (username and password)

### I reccomend you do this everytime you are finished coding for the day. That way we can track past and present versions of your work, utilizing Github's version control system.

# Step 4 : Do this part if you have finished something and want to "submit your final answer".
- Go to github and make a pull request. 
- To make your first pull request go to your repository on GitHub and you will see a clickable green button on the top right corner “Compare & pull request”. Click on it.
- At the bottom of the page add a description of what changes you have made.
- Congratulations! You've just made your first pull request.

- Note : A pull request is where we evaluate and finalize your submitted work, and make any possible changes. In the industry, this process is also known as       "code review". 
- To learn more about how to make a pull request you can refer to this link for the official guide: https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request 

# Future Changes and Wants
    - Make Bot Mode like an actual bot, reacting to common messages that needs to be responded.
    - Shift to user and bot mode in any form of time, it is not only limited to after a new member joining
    - MAke a channel where they can talk to the bot asking some common or repetitive questions, if it is not in this channel the bot does not reply appropriately.

