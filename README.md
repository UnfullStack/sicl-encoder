# sicl-encoder
## S.I.C.L. - Silly Image Compression Lossy. This probably doesn't actually save space, but it's nice to imagine.

### Limitations
SICL only works for images with a max width of 256 and 256 colors. The Python encoder will account for colors and quantize the image if there are too many colors, but does not resize the image if it is too large.

### Explanation
SICL works by indexing colors in an array.

SICL is split up into what I'll call "chunks". Chunks can range from just 1 byte to thousands or more. It's just how the file is split up, there's no specific size.

| Chunk | Data | Bytes |
|--|--|--|
| 1 | Amount of colors | 1 |
| 2 | Colors (RGB) | Variable, 3 per entry |
| 3 | Image width | 1 |
| 4 | Color indexes |  Variable, 1 per entry |

Height doesn't need to be saved because color indexes are sorted left to right, so you can just use the width and amount of indexes to find the height.
