# ePyHTML
Version: 0.3
## How to Install?
1. __Clone__ the code
2. __Move__ the downloaded ___ePyHTML___ folder to your project directory
3. __Create__ a New __Python__ File in your project directory
4. __Import__ the library by:
    ```python
    from ePyHTML import ePyHTML
    ```
   __Import__ with alias:
    ```python
    from ePyHTML import ePyHTML as ePH #you can rename 'ePH' whatever you want
    ```
   
## How to use?:
  Create the html file by coding:
  ```python
  from ePyHTML import ePyHTML
  ePyHTML.startHTML("file name", extension="html", title="html title", css_path="./file.css")
  ```
  * The first parameter in `startHTML()` is the file name (necessary)

  * Other parameters are _`extension`_ , _`title`_ and _`css_path`_ (not necessary)

  * Parameter _`exetension`_ is for the file extension, no need to use this parameter if you want to create a __HTML__ file.

    * __HTML__ is the default extension, if you want a PHP file, do it by:

      ```python
      from ePyHTML import ePyHTML
      ePyHTML.startHTML("example", exetension="php", title="title example")
      ```
   * Parameter _`title`_ is for the __HTML__ `<title>` tag, no title by default value
   * Parameter _`css_path`_ is for the __HTML__ `<link rel="stylesheet" href="./file.css">` tag, no external CSS stylesheet by default
  ### h1 to h6 tags
  ```python
  from ePyHTML import ePyHTML as ePH
  ePyHTML.startHTML("file name", extension="html", title="html title")
  ePH.heading1("text", classname="text", id="text", center=1)
  ePH.heading2("text", classname="text", id="text", center=1)
  ePH.heading3("text", classname="text", id="text", center=1)
  ePH.heading4("text", classname="text", id="text", center=1)
  ePH.heading5("text", classname="text", id="text", center=1)
  ePH.heading6("text", classname="text", id="text", center=1)
  ```
  * First parameter is the text for the h1 to h6 tags (necessary)
  * Parameter `classname=""` is the parameter to create a `class` for the specific tag (not necessary)
  * Parameter `id=""` is the parameter to create an `id` for the specific tag (not necessary)
  * Parameter `center=` is the parameter to make it justified in the center of the page (not necessary)
    * `center=0` is the default value, enter `center=1` to make the tag center-justified 
    
  ### a tag for _href_
  ```python
  from ePyHTML import ePyHTML as ePH
  ePyHTML.startHTML("file name", extension="html", title="html title")
  ePH.url("text", classname="text", id="text", url="https://github.com/MCTVR/ePyHTML", center=1)
  ```
  * First parameter is the text for the a tag (necessary)
  * Parameter `classname=""` is the parameter to create a `class` for the specific tag (not necessary)
  * Parameter `id=""` is the parameter to create an `id` for the specific tag (not necessary)
  * Parameter `url=""` is the parameter for the _href_ site __URL__ (not necessary)
    * enter the website into it, press it to redirect to the __URL__ you entered
  * Parameter `center=` is the parameter to make it justified in the center of the page (not necessary)
    * `center=0` is the default value, enter `center=1` to make the tag center-justified 

  ### p tag for paragraphs
  ```python
  from ePyHTML import ePyHTML as ePH
  ePyHTML.startHTML("file name", extension="html", title="html title")
  ePH.paragraph("Lorem ipsum dolor sit amet", classname="paragraph", id="paragraph", center=1)
  ```
  * First parameter is the text for the `p tag`, use `"""` for multiple lines (necessary)
  * Parameter `classname=""` is the parameter to create a `class` for the specific tag (not necessary)
  * Parameter `id=""` is the parameter to create an `id` for the specific tag (not necessary)
  * Parameter `center=` is the parameter to make it justified in the center of the page (not necessary)
    * `center=0` is the default value, enter `center=1` to make the tag center-justified 
    
  ### img tag for images
  ```python
  from ePyHTML import ePyHTML as ePH
  ePyHTML.startHTML("file name", extension="html", title="html title")
  ePH.img(src="https://avatars.githubusercontent.com/u/69135058", classname="image", id="image", center=1)
  ```
  * `src=""` parameter is the *URL* or *local path* of the image for the __HTML__ equivalent `img tag`(necessary)
  * Parameter `classname=""` is the parameter to create a `class` for the specific tag (not necessary)
  * Parameter `id=""` is the parameter to create an `id` for the specific tag (not necessary)
  * Parameter `center=` is the parameter to make it justified in the center of the page (not necessary)
    * `center=0` is the default value, enter `center=1` to make the tag center-justified 
  
  ### Finish the script by adding `finHTML()`
   ```python
   from ePyHTML import ePyHTML as ePH
   ePyHTML.startHTML("file name", extension="html", title="html title")
   ePH.heading1("text", classname="text", id="text", center=1)
   ePH.heading2("text", classname="text", id="text", center=1)
   ePH.heading3("text", classname="text", id="text", center=1)
   ePH.heading4("text", classname="text", id="text", center=1)
   ePH.heading5("text", classname="text", id="text", center=1)
   ePH.heading6("text", classname="text", id="text", center=1)
   ePH.url("text", classname="text", id="text", url="https://github.com/MCTVR/ePyHTML", center=1)
   ePH.finHTML()
   ```
   ## Effect:
   <img src="https://i.imgur.com/BOhScLm.png?1" />
   <img src="https://i.imgur.com/4lYhCpD.png?1" />
   
   ## Browser Effect
   <img src="https://i.imgur.com/p765EKE.png" />
