# Scraping and Chunking

## Prerequisites

Apply for a Google API key.

https://aistudio.google.com/app/apikey

## Install

```bash
pip install -r requirements.txt
```

## Run

Set the `GOOGLE_API_KEY` environment variable, then run the script.

```bash
export GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
python main.py
```

## Error recovery

Just run the script again. It will pick up where it left off.

## Demo output

```bash
https://www.notion.so/help/images-files-and-media

Chunk 1: 925
Images, files & media
Add more color to your Notion page by uploading images, videos, audio, and more 🎞️
Media block types
Images
Notion makes it easy to add, resize, and arrange images in any configuration or format (JPG, PNG, GIF, etc.). You can drag and drop an image into a Notion page, or you can upload an image as a block in your page. To do this:
Click the + that appears in your left margin when you hover over a new line. Choose Image and press enter. Or, type /image and press enter.
Click to upload an image from your computer, embed an image from elsewhere using its URL, or add a stock photo from Unsplash.
Images can also be hyperlinked, so that people can click on them to navigate to the URL of your choice. To add a hyperlink to an image:
Hover over the image and select ••• or ⋮⋮ → Add link.
Paste a link or select a Notion page as the destination. If you choose a Notion page, a backlink won’t be created.

Chunk 2: 934
You can also add images to databases, and display them as a gallery. Learn more about gallery view here →
In a database, add the Files & media property. Clicking that field gives you the option to upload an image from your computer or embed an image from elsewhere.
Drag an image file into a card on a database board, or into a Files & media property cell in a table, or into a gallery.
Of course, you can also add an image to the body of any page inside a database using /image or drag-and-drop.
Files
Keep your files in Notion to easily store and share them. At any place on your page, create a file block that will prompt you to Upload a file from your computer or use an Embed link to embed a file on your page like a PDF.
Looking to import content into Notion? See the instructions in this article →
Click the + that appears to the left when you hover over a new line. Choose File and press enter. Or, type /file and press enter.

Chunk 3: 983
A menu will pop up giving you the Upload or Embed link options. Select the file you want and click Open.
You can also drag files into a Notion page from your desktop or a folder on your computer. Notion will upload and safely store it for future access and download.
You can also add files to databases to associate them with other information. For instance, you're creating a library of assets and you want to add tags and other context to each asset.
Add the Files & media property to your database.
Click on that property (like a cell in that column of a table). You'll be prompted to upload your own file or embed a file from elsewhere.
You can also drag and drop files into cells under this property in a table. Or you can drag them into cards on a board or in a gallery. They'll appear in the Files field of the corresponding pages.
Videos
Anywhere on your Notion page, you can add a video from any streaming service that offers embed links. There are a couple ways to do this:

Chunk 4: 979
Click the + that appears to the left when you hover over a new line. Choose Video and press enter. You can also type /video and press enter.
In the menu that appears, select Embed link, then paste the video's share URL from the streaming service and click Embed video.
As an alternative method, simply paste a video's URL from a streaming service. In the menu that appears, choose Create embed.
You can also upload your own video files to play in our custom player.
Click the + that appears to the left when you hover over a new line. Choose Video and press enter. You can also type /video and press enter.
In the menu that appears, select Upload, and choose your video file.
You can also drag your video file into a Notion page from your desktop or a folder on your computer. Notion will automatically convert it to our custom video player.
Note: If your browser or OS supports playback of this video/audio format, you’ll be able to play it directly from within the Notion page.

Chunk 5: 1015
If your browser or OS does not support playback of this video/audio format, this content may not be directly playable.
Audio
Anywhere on your Notion page, you can add audio from most streaming platforms:
Click the + that appears to the left when you hover over a new line. Choose Audio. You can also type /audio and press enter.
In the menu that appears, select Embed link, and paste the URL for the track or playlist from your streaming service.
Or, simply paste the track or playlist's URL from the streaming service. In the menu that appears, choose Create embed.
Alternatively, you can upload an audio file directly from your computer.
Click the + that appears to the left when you hover over a new line. Choose Audio and press enter. You can also type /audio and press enter.
In the menu that appears, select Upload, and choose your audio file.
You can also drag your audio file into a Notion page from your desktop or a folder on your computer. Notion will automatically convert it to our custom audio player.

Chunk 6: 776
Note: If your browser or OS supports playback of this video/audio format, you’ll be able to play it directly from within the Notion page.
If your browser or OS does not support playback of this video/audio format, this content may not be directly playable.
Web bookmarks
There are a few ways to add a web bookmark to a page:
Click the + displayed to the left when you hover over a new line. Choose Web Bookmark and press enter.
Type /web bookmark or just /bookmark and press enter.
In the mobile app, paste a URL and select Create bookmark.
Each method asks you to enter the URL. Press enter and your bookmark will pop up.
Media block options
Arrange & resize
To arrange: Use drag and drop to move a media block around your Notion page. You can drag them into columns as well.

Chunk 7: 885
To resize: Hover over your media block and you'll see two black guides appear on the left and right edges. Click either one and drag to make your video bigger or smaller.
Crop
Hover over an image and select ••• → Crop image.
Once you’re finished, select Save.
Mask
Hover over an image and select ••• → Crop image.
Select the shapes icon in the top left corner and choose your masking dimensions.
Once you’re finished, select Save.
Align
Hover over any image, file or media block and click the alignment icon. This appears as a square with lines above and below.
Choose to align left, center, or right.
Caption
Hover over any image, file or media block and click the caption icon. This appears as a square with lines underneath, representing captions below media.
You'll see gray text appear below your image, file or media. You can edit and style this like any other text on your page.

Chunk 8: 824
Alt text
Hover over an image and select ••• → Alt text.
Add alt text describing your image and hit enter when you’re done.
You can hover over ALT in the corner of an image to see its alt text.
Make sure your alt text is short and descriptive. You can also provide specific details based on the context of the page that your image is embedded in. For example, if you’re including an image in a page about teaching, you could say “Teacher talks to student in the classroom” instead of “Two people talk in a room”.
Download
On desktop
Hover over any image, file, or media and click the download icon on its top right. This appears as a downward-facing arrow inside a circle.
This will save the file on Notion to your computer.
On mobile
Tap the ••• at the top right of the image, file or media block, then select View original.

Chunk 9: 822
The image, file, or media will open in an in-app browser. Long press on the image to add it to your photo roll.
View original or full-screen
You can view images in Notion in a couple other ways — in its original format inside your browser, and in full screen mode. Here's how:
Hover over any image, file, or media and click Original. This will open the image in its original size inside a new tab on your browser.
For full screen, hover on the image and click •••. Choose Full screen from the dropdown. (You can also select the image and press space).
Replace
You can replace images, files, or media in Notion with a different one in the same exact size/spot.
Hover over the block and click •••. Choose Replace. This will open a window where you can upload another file from your computer or embed an image from elsewhere.

Chunk 10: 768
Comment
Like you can with text or any other content block in Notion, you can add a comment to an image, file, or media block.
Hover over any image, file, or media and click the word bubble icon.
Or, hover over and click •••. Choose Comment. You can type @ followed by someone's name to mention any of your teammates and call their attention to a question, suggestion or idea you have about the image.
Delete
Hover over any image, file, or media and click ••• at the top right or ⋮⋮ on the left. You can also right click on the block itself.
Choose Delete.
FAQs
Why do I not see alignment controls on my image, file or media block?
The alignment controls are hidden if the block is the same width as content on the page, or if the block is already at its maximum width.

Chunk 11: 444
Are there size limits for images and files?
While you can upload an unlimited number of images and files into Notion, there are limits on the size of each image and file.
If you’re on the Free Plan, you can upload files of up to 5MB each. If you’re on a paid plan, you can upload files of up to 5GB each. If you upload an image and get an error telling you that the image is too large to be displayed, you can try uploading the image as a file.
```
