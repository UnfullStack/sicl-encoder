# sicl-encoder
### S.I.C.L. - Simple Image Compression Lossy. (Sickle)
### This probably doesn't actually save much, if any space, but it's nice to imagine.

#### Limitations
SICL only works for images with a max width of 256 and 256 colors. The Python encoder will account for colors and quantize the image if there are too many colors, but does not resize the image if it is too large.

#### Explanation
SICL works by indexing colors in an array.

SICL is split up into what I'll call "chunks". Chunks can range from just 1 byte to thousands or more. It's just how the file is split up, there's no specific size.

| Chunk | Data | Bytes |
|--|--|--|
| 1 | Amount of colors | 1 |
| 2 | Colors (RGB) | Variable, 3 per entry |
| 3 | Image width | 1 |
| 4 | Color indexes |  Variable, 1 per entry |

Height doesn't need to be saved because color indexes are sorted left to right, so you can just use the width and amount of indexes to find the height.

## .sicl2 format
The script does not yet support this format, and I haven't created any files with it, but the idea is fairly simple: Remove some of the limitations of the format (or at least make them much more favorable) by increasing both the width and color count from taking up 1 byte each to 2 bytes each.

## Notes
I'm sure people who are familiar with working with files like this are wondering why I don't have a header like PNG or JPG do. In all honesty, while I did consider it, I ended up deciding not to, as it's not like I'm planning to make this the new standard or something like that. It's a project I did for fun, and I'm not exactly worried about identifying this.
