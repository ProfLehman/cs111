Yes — here is the revised page with **CSV, HTML, and JSON added**, and **BMP/WebP removed**.

# Common File Formats

A **file format** defines how information is organized and stored in a computer file. The **file extension**, such as `.txt`, `.jpg`, or `.pdf`, usually identifies the format and helps the operating system determine which programs can open the file.

Different formats are designed for different types of data. Some formats also use **compression** to reduce file size. **Lossless compression** reduces file size without discarding information, while **lossy compression** reduces file size by permanently removing some information.

## Text and Data Formats

### TXT (`.txt`)

A **TXT file** contains plain text without document formatting such as fonts, colors, images, or page layouts. The characters in a text file must be represented using a character encoding such as **ASCII** or **UTF-8**. The `.txt` extension does not specify which character encoding is being used, although UTF-8 is common today. Text files are simple, portable, and can be opened by almost any text editor.

**Reference:** [Wikipedia overview for text files]([https://www.iana.org/assignments/media-types/text/plain](https://en.wikipedia.org/wiki/Text_file)

### CSV (`.csv`)

**CSV (Comma-Separated Values)** is a simple text-based format used to store data in rows and columns. Each line normally represents one row of data, and values are separated by commas. CSV files are commonly used to transfer data between spreadsheets, databases, and programs. Because CSV stores plain text rather than formulas, formatting, or charts, it is simpler than an Excel workbook and can be processed easily by programs such as Python.

Example:

```text
Name,Major,Year
Maria,Biology,2
Jordan,Computer Science,1
Taylor,Business,3
```

**Reference:** [IETF RFC 4180 — Common Format and MIME Type for CSV Files](https://www.rfc-editor.org/rfc/rfc4180)

### JSON (`.json`)

**JSON (JavaScript Object Notation)** is a text-based format used to store and exchange structured data. JSON organizes information using structures such as **name/value pairs** and **lists**. It is widely used by websites, web services, APIs, configuration files, and programming applications. Although JSON originated from JavaScript, it is now supported by most modern programming languages, including Python.

Example:

```json
{
  "name": "Maria",
  "major": "Biology",
  "year": 2
}
```

**Reference:** [IETF RFC 8259 — The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259)

## Document and Spreadsheet Formats

### PDF (`.pdf`)

**PDF (Portable Document Format)** was developed by Adobe for storing and exchanging documents while preserving their appearance across different computers and operating systems. A PDF can contain text, fonts, images, graphics, hyperlinks, forms, and other content. PDF is now an open standard maintained by the **International Organization for Standardization (ISO)** as ISO 32000. PDFs are commonly used when a document needs to be viewed or printed with a consistent layout.

**Reference:** [Adobe — What is PDF?](https://www.adobe.com/acrobat/about-adobe-pdf.html)

### DOCX (`.docx`)

**DOCX** is the standard document format used by modern versions of **Microsoft Word**. It is part of the **Office Open XML (OOXML)** family of formats and can store formatted text, images, tables, styles, and other document information. A DOCX file is actually a collection of XML files and other resources packaged together in a **ZIP-based container**.

**Reference:** [Microsoft — Open XML Formats and File Name Extensions](https://support.microsoft.com/en-us/office/open-xml-formats-and-file-name-extensions)

### XLSX (`.xlsx`)

**XLSX** is the standard workbook format used by modern versions of **Microsoft Excel**. Like DOCX, it is part of the **Office Open XML (OOXML)** family and uses a ZIP-based container to hold XML files and other resources. An XLSX workbook can contain worksheets, formulas, numbers, text, charts, formatting, and other spreadsheet information. Files containing Excel macros normally use the `.xlsm` extension instead.

**Reference:** [Microsoft — Open XML Formats and File Name Extensions](https://support.microsoft.com/en-us/office/open-xml-formats-and-file-name-extensions)

## Web Formats

### HTML (`.html`)

**HTML (HyperText Markup Language)** is the standard markup language used to describe the structure and content of web pages. An HTML file is a text file containing **elements** or **tags** that identify items such as headings, paragraphs, links, images, tables, and lists. A web browser reads the HTML and displays the page based on those instructions.

For example:

```html
<h1>My Web Page</h1>
<p>This is a paragraph.</p>
```

HTML describes the structure of a web page, while technologies such as **CSS** control its appearance and **JavaScript** can add behavior and interactivity.

**Reference:** [WHATWG — HTML Living Standard](https://html.spec.whatwg.org/)

## Common Image Formats

### JPEG (`.jpg` or `.jpeg`)

**JPEG (Joint Photographic Experts Group)** is one of the most common formats for photographs and images containing many colors and gradual changes in color. JPEG primarily uses **lossy compression**, which reduces file size by permanently removing some image information. Increasing the amount of compression produces smaller files but may also reduce image quality. JPEG works especially well for photographs but is usually less suitable for diagrams, text, or images requiring transparent backgrounds.

**Reference:** [JPEG — JPEG Standard](https://jpeg.org/jpeg/)

### PNG (`.png`)

**PNG (Portable Network Graphics)** uses **lossless compression**, meaning that an image can be compressed and reconstructed without losing its original image data. PNG is commonly used for screenshots, diagrams, logos, and images containing text or sharp edges. It also supports an **alpha channel**, which allows pixels to be partially or completely transparent. PNG files are often larger than comparable JPEG photographs because PNG does not discard image information.

**Reference:** [W3C — Portable Network Graphics (PNG) Specification](https://www.w3.org/TR/png-3/)

### GIF (`.gif`)

**GIF (Graphics Interchange Format)** is an older image format that uses **lossless compression** but is limited to a palette of at most **256 colors per image frame**. This makes GIF appropriate for simple graphics, icons, diagrams, and images with relatively few colors, but less appropriate for photographs. GIF also supports transparency and can store a sequence of images to create simple **animations**.

**Reference:** [W3C — GIF89a Specification](https://www.w3.org/Graphics/GIF/spec-gif89a.txt)

### HEIC (`.heic`)

**HEIC** is commonly used for photographs captured by modern Apple devices such as the iPhone. These files typically use the **HEIF (High Efficiency Image File Format)** container and store images compressed using technologies such as **HEVC (High Efficiency Video Coding)**. HEIF/HEVC can produce high-quality images using less storage space than comparable JPEG files. Compatibility is not as universal as JPEG, so devices and applications may convert HEIC images to JPEG when they are shared.

**Reference:** [MPEG — HEIF Image File Format](https://www.mpeg.org/standards/MPEG-H/12/)

See also: [Apple — Using HEIF or HEVC Media on Apple Devices](https://support.apple.com/en-us/116944)

## Audio Formats

### MP3 (`.mp3`)

**MP3** is a widely used digital audio format based on **MPEG Audio Layer III**. MP3 uses **lossy compression** to substantially reduce the amount of data needed to store audio. The compression process takes advantage of characteristics of human hearing and removes or stores with less precision some audio information that is less likely to be noticed. This allows music and other audio recordings to use much less storage space than uncompressed digital audio.

**Reference:** [Fraunhofer IIS — MP3](https://www.iis.fraunhofer.de/en/ff/amm/consumer-electronics/mp3.html)

## Video Formats

### MP4 (`.mp4`)

**MP4 (MPEG-4 Part 14)** is a widely used **container format** for digital video and audio. An MP4 file can contain video, audio, subtitles, images, and other data. The MP4 format itself does not specify how the video or audio must be compressed; instead, it can contain media compressed using different **codecs**, such as **H.264** for video and **AAC** for audio. MP4 is commonly used for streaming video, recording video on phones and cameras, and sharing video over the Internet.

**Reference:** [MPEG — MPEG-4 File Format](https://www.mpeg.org/standards/MPEG-4/14/)


## Archive and Compression Formats

### ZIP (`.zip`)

A **ZIP file** is an **archive format** used to combine one or more files and directories into a single file. ZIP commonly applies **lossless compression**, meaning that the original files can be reconstructed exactly when the archive is extracted. ZIP files are useful for reducing storage requirements, grouping related files together, and transferring collections of files.

**Reference:** [PKWARE — ZIP File Format Specification](https://support.pkware.com/home/pkzip/developer-tools/appnote)

--end--
