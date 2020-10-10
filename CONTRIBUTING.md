# Step by Step Guidelines on Contributing

# Step 0 : What is Github?  ( Optional)

#### I reccomend you watch this video to get a basic gist of how github works and the process we are conducting.
Link : https://www.youtube.com/watch?v=w3jLJU7DT5E

# Step 1 : Install Git in your machine

Please install Git in your machine, for you to be able to use it in your respective command line/terminals. (Also known as cmd in windows, and Terminals in Unix Machines)

Use this link as reference.
Link: https://www.atlassian.com/git/tutorials/install-git

# Step 2 :  Fork this Repository
There is a clickable button in your top-right called "Fork", click on it and it will give a copy of my entire repository to you.


# Step 3 : Submitting the work

After forking the repositiory go to the repository which you will now be able to see on your profile. Once in the GitHub repo, click on the green button that says, "Clone or download". A dropdown will show you a password protected SSH key. You can change it to HTTP by clicking "Use HTTPS" in the upper right-hand corner of that dropdown. Copy the link from there. Now open the terminal and write these commands.

- Type the command : ```git clone {HTTPS ADDRESS}```
- Type the command : ```cd {NAME OF REPOSITORY} ```
- This will create a local copy of the repository on your machine.
- Now Go to the repository/directory/folder where this copy of the repository is saved.
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
