# MediaGoblin-Heroku

A project dedicated to making [GNU MediaGoblin](http://mediagoblin.org) easily deployable to [Heroku](http://heroku.com).

## Notes

* I couldn't get Celery and the message broker working the way I wanted to, so for simplicity, I have [CELERY\_ALWAYS\_EAGER](http://docs.celeryproject.org/en/latest/configuration.html#celery-always-eager) turned on. If you figure out a way to get an external queue working on Heroku with MediaGoblin, send a pull request and I'll gladly accept it.
* While you can store everything locally on Heroku, it's recommended that you setup [Rackspace Cloud Files](http://www.rackspace.com/cloud/files/) to store the data files to prevent going over your quota. Instructions to perform this can be found [here](http://wiki.mediagoblin.org/Configure_MediaGoblin#Setting_up_Cloud_Files_public_storage).

## Set-up

1. Clone the repository:

  ```sh
  git clone git@github.com:frewsxcv/mediagoblin-heroku.git
  cd mediagoblin-heroku
  ```

2. Install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

3. Create your app on Heroku. If you plan on using [Heroku Postgres](https://postgres.heroku.com/), make sure to install that as well.

4. Add your Heroku app remote to the local git repository:

  ```sh
  heroku git:remote -a <your Heroku app name here>
  ```

5. Copy the template config file and modify it to suit your needs:

  ```sh
  cp mediagoblin.tmpl.ini mediagoblin.ini
  ```

6. Commit your config file to your local repo:

  ```sh
  git commit -m "Add my config file" mediagoblin.ini
  ```

7. Push to your remote Heroku repository:

  ```sh
  git push heroku master
  ```

  This will deploy MediaGoblin to Heroku. Be patient with this process as MediaGoblin has quite a few Python dependencies.

## License

MediaGoblin-Heroku is licensed under [version two of the Mozilla Public License](LICENSE.md). MediaGoblin licensing information can be found in [their repository](https://gitorious.org/mediagoblin/mediagoblin/source/HEAD:COPYING).
