# MediaGoblin-Heroku

A project dedicated to making [GNU MediaGoblin](http://mediagoblin.org) easily deployable to [Heroku](http://heroku.com).

## Set-up

1. Clone the repository:

```sh
git clone git@github.com:frewsxcv/mediagoblin-heroku.git
cd mediagoblin-heroku
```

More instructions coming soon

## Database

By default, MediaGoblin-Heroku will use a SQLite database. If there is an environment variable named `DATABASE_URL` containing a database connection URL (which is the case if you have [Heroku Postgres](https://postgres.heroku.com/) installed), then MediaGoblin will use PostgreSQL.

## License

MediaGoblin-Heroku is licensed under [version two of the Mozilla Public License](LICENSE.md). MediaGoblin licensing information can be found in [their repository](https://gitorious.org/mediagoblin/mediagoblin/source/HEAD:COPYING).
