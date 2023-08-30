# How To Get Transcripts For Any Podcast

Created: January 23, 2023 9:41 AM
URL: https://markallen.io/podcast-transcripts/
Durée: 184

![profile-pic.jpg](How%20To%20Get%20Transcripts%20For%20Any%20Podcast%204bcc8cc6428b4d54ae49535ab8bee8ae/profile-pic.jpg)

One thing that annoys me about the rise of podcasts as a knowledge-sharing medium is how hard it is to capture and recall information later. Like most people, I listen to podcasts while walking, doing the dishes, driving, or doing any number of other things where you can’t easily take notes while listening.

In a perfect world, every podcast would have a transcript, and I could just press a button in my podcast player to send a text snippet to my notes app. Sadly, that world doesn’t exist. But you can still get pretty close if you’re willing to jump through enough hoops.

By the end of this post, you’ll know how to generate transcripts for snippets of a podcast directly from your podcast player, and create the full transcript for any podcast you listen to.

## Tools we’ll be using

This workflow is based on the apps I already use on iOS, so you may need to make some substitutions to work with your setup.

- **[Overcast](https://overcast.fm/)** is the best iOS podcast player, and we’ll be using its [clip sharing](https://marco.org/2019/04/27/overcast-clip-sharing) feature to grab snippets up to 90 seconds.
- **[Otter.ai](https://otter.ai/)** is the service we’ll use to do the audio to text transcription. You can sign up for a free plan that gives you 600 minutes of transcription a month or upgrade to 6,000 minutes for $8.33 USD per month.
- **[This Apple Shortcut](https://www.icloud.com/shortcuts/225beffca1a64b3f9f63f23da5a02c00)** is how we will get the podcast’s mp3 source information from Overcast. If you are on Android, you’ll need to figure out another way to do that.
- **[Drafts](https://getdrafts.com/)** is the iOS note app I use as an inbox. If you prefer another app (anything from Apple Notes to Evernote or even an email), you can easily adjust the Shortcut above to work for you. We need this for the full episode transcript workflow because of a minor Otter shortcoming discussed below.

## Getting the transcript for an audio clip

Let’s start with getting the transcript for a snippet of up to 90 seconds, which is what I do most often. We’ll be using some of the same steps for getting a full episode transcript later on, so it’s a good place to start.

1. While listening to a podcast in Overcast, tap the Share icon to pull up the sharing menu.
2. Select “Share Clip…”
3. On this screen, you can edit the clip start and endpoints. Make sure you select “Audio only” to create an audio file instead of a video.
4. Tap the Share icon on the next screen to open the sharing menu.
5. Once you select Otter in the sharing menu, the audio clip will be uploaded to be processed, and you can back to listening to your podcast.

After you’ve uploaded a clip to Otter, the transcript will be available in the Otter app and on website, usually in just a minute or so.

## Getting transcripts for full episodes

Generating the transcript for an entire podcast episode is more complicated if you’re listening on your phone. Otter lets you import files, but Overcast (like most podcast players) doesn’t make it easy to get to the source URL of a podcast episode, which is where the Shortcut action and Drafts note come in to play.

1. Like the audio clip workflow, start by tapping the Share icon to pull up the sharing menu.
2. This time, you’ll select the “Share Link” option.
3. Choose the “Add Podcast Source File To Drafts” shortcut. You may need to dig around in the “Edit Actions…” menu to surface this shortcut. In case you can’t find it, make sure you installed it from [this link](https://www.icloud.com/shortcuts/225beffca1a64b3f9f63f23da5a02c00).
4. The shortcut action will run automatically, you just need to wait a moment for it to complete.
5. If you open Drafts on your iPhone or Mac, you’ll see a new note created with the episode information. Download the URL listed under “Source file” to get the actual MP3 that we’ll use next.
6. From your Otter dashboard, click the “Import audio/video” button and select the file you downloaded in the previous step.

After you’ve uploaded the episode, Otter will generate a transcript within a few minutes.

[Here’s a video](https://twitter.com/moustache/status/1269281784761589760) of the whole workflow in action. The whole processs is simple after you set it up once.

If you want, you can do steps 5 and 6 all from iOS with the Otter app, but I find that downloading files to my phone and then uploading them again is too much of a hassle to bother. So far, capturing the info to Drafts and just doing it when I’m back on my computer is good for me.

Otter could make this workflow easier if they supported file imports via a URL. We could then skip steps 5 and 6 altogether, and I’d probably be able to rewrite the Shortcut action to send Otter the link directly. But that’s a bit of an edge case for the Otter team to support, and this still works without that option.

## Customizing this workflow

I can see a few ways you may want to change things in this process based on how you listen to podcasts. If you don’t use Overcast, there may be a way to get a link to the mp3 source file for the episode from your podcast player. If you don’t use Drafts, it’s pretty easy to edit the Shortcut action to use the app of your choice. If you are feeling daring, you could try to extend the shortcut to automatically download the mp3 to the Files app or Dropbox and then automatically send that to Otter.

Let me know how this workflow works out for you on [Twitter](https://twitter.com/moustache). If you get stuck anywhere, I’ll be happy to try and help you figure it out. Good luck!