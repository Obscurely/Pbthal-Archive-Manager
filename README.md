# Pbthal Archive Manager

This is a set of python scripts wrapped in a cli to
- dowload
- extract
- mass rename
- make proper albums by changing the tags
- create spectrograms
- broken for now, download albums covers

## Requirements

This script uses https://real-debrid.com/ to download files for file factory which requires a subscription (file factory does to). The difference is this is cheaper and it also works with multiple websites.

What you need to do after getting a subscription is get your bearer auth token. To do this open your browser dev tools, go to the network tab, request a download from file factory or something, click on that request and from the headers copy the auth token.

Paste that in a ".env" file in the root of this project. It should look something like this.

bearer=Bearer SOMETHINGSOMETHING

"bearer=" is the key and after that is the value, the thing you copied.

## Instructions

The way to do it would be (using poetry)

1. Search for albums to download

Unlike pbthal's website this is an exact search. So it searches for results that 100% contain your query so you can actually find something.

```
po run python3 pbthal_archive_manager/__main__.py s Metallica Master of Puppets
```

Look for the archive you want to download from and copy the file factory link somewhere

2. Download the archives

So you would run

```
po run python3 pbthal_archive_manager/__main__.py d
```

Then paste one by one in each input the links to the archives you want to download. When you are done just hit enter and it will start downloading them with real debrid.

3. Extract all the archives

```
po run python3 pbthal_archive_manager/__main__.py e
```

This will extract all the archives present in the downloads folder

4. Mass rename if you want

This will only work on linux properly

```
po run python3 pbthal_archive_manager/__main__.py r
```

This will go through every folder in music and prefil your input so you can edit them one by one by hitting enter and renaming where the case is.

5. Downloading album covers

This is broken for now.

```
po run python3 pbthal_archive_manager/__main__.py c
```

This will get every folder's name from music and in that folder download a cover under the name Cover.jpg

If download manually a cover make sure it's named Cover.jpg

6. Make the albums

```
po run python3 pbthal_archive_manager/__main__.py a
```

This will go into every folder properly change the metadata tags for every flac file and also create spectrograms of every flac file. You can delete the spectrograms, I just like to have them.
