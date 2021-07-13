
# Procedural Building Generator Blender add-on
 I'm Alex Morales Garcia, student of the Game Development Bachelor Degree at CITM (Terrassa). This is a Procedural Building Generator add-on for Blender.

## Installation
-   Open Blender and create a new scene.
    
-   Go to Edit > Preferences…
 
-   Click the “Install” button, on the top right of the window.
    
-   Search the add-on zip and when clicked it will be installed.
    
-   On the right of the scene window, will appear a tab named PBG and the add-on is ready to be used.

## About

PBG add-on allows you to procedurally generate different buildings by modyfing different in the different modules. There are a total of 5 modules:

-   **Module Window:** The window can be modified with different parameters:
	- Size
	- Frame width
	- Type (Vertical, Horizontal, Cross)
	- Frame color
	- Glass color

-  **Module Door:** The door can be modified with different parameters:
	- Size
	- Frame width
	- Frame color
	- Glass color

-  **Module Wall:** The wall can be modified with different parameters:
	- Texture on/off
	- Two colors on/off
	- Wall texture
	- Wall color

-  **Module Balcony:** The wall can be modified with different parameters:
	- Window size
	- Outter size
	- Frame width
	- Frame color

## How it works
The tool appears as a tab in the VIEW 3D lateral menu. The tab name is PBG, which is an acronym for Procedural Building Generation. The tool is divided in one main panel, where the building structure and facade can be modified. Underneath, there are four different sub panels: window, wall, balcony and roof. There is a fifth panel but only is used for debugging the tool.

The main sub panel allows the user to modify the following parameters:

-   Module size: The width and depth of each module. At this moment, all the modules have the same size.
    
-   Building size: The number of floors, and the module number in X and Y axes. This would be the base structure of the building.
    
-   Floor randomness: The level of randomness between the floors. When it is 0, the modules and structure will be identical to the previous one. On the contrary, if it is 5, the floors are completely different from each other.
    
-   Building type: There are three different types of buildings: flat, random and symmetrical. The flat has all the faces flat, with no perturbation between them. The random faces have an inconsistent floor. The symmetrical building has each side symmetrical to the middle of the current side.
    
-   Building position: This is the position of the building on the street. There are three different options: solo, middle or corner. When it is solo, it has the 4 sides generated, when it is middle, it only generates the front and back faces of the building, leaving the others flat. If it is a corner, it creates three consecutive faces.
    

In the figure below we can see an image of the interface in Blender. When the building is generated, the whole panel disappears as the building cannot be modified once it is created.

**![](https://lh5.googleusercontent.com/51yJZ0PKnx9hlOeLbFCvpfd79i4AanhNxqwchCxCBTF57QXA8_wqYB8PcZAnKUF9-6r2lOXpESWmONGwCOBpy4JnnwurduYdxLML_blVcyP_aJIs2COUkidw3QwOggBl4eZ1Crk)**

### Window sub panel

This sub panel allows modification of the window construction and texture parameters. It is composed of two boxes. The first one is the “Construction parameters” box, which modifies the window width and height and the frame width. What’s more, the frame width can be modified too. Lastly, there are three different window types: vertical, horizontal and cross.

The second box is “Texture parameters”, which contains two color wheels, one for the window frame color and other for the glass window color. We can see the interface on Figure 5.7.

![](https://lh5.googleusercontent.com/rGQPmNU_6Cuk8iSwhuqHlDhsAsFtATJ3-CH5lO0dn-x9WdoriJMG_slmAcum03U1cCDk_NbV9kWXiuCdCPz-3xJJsdKhj-99Lf3-8rp-KlafHn9RmTz2MHEcR8KqDnNI9WqSaoU)

### Wall subpanel
This panel is in charge of controlling all the parameters related to the exterior walls of the building. The user can decide if is using a texture or a base color. If it is using a texture, there are three that can be chosen: brick, stone and wood. Whereas it is not using one, we can modify the building base color. There is also an option to use two different colors when creating a building.

![](https://lh4.googleusercontent.com/SCW0DZMATrd9Owap7D8Bj1TT2QokapUaQz4UmQ4Y2CT0BwxxjOnyAol7WKOUzB5rF-SA6wNkTVRc_SpgOK1JxbKBUSok3v72ULRGBX56AHGme9VTC-sNMlyODnk5uJWpoV25zsw)

![](https://lh6.googleusercontent.com/VdiBObda60uF3BchxdYDutkQSSPYBNZxqQCpWjDvCnaN-SIG7xW4b4dEzGpEWHRiFZHyerURnpF-NpU9IoqIcmg0EeGhUQgiMZEbzK82JHGlKTKRjEgPrTLRssiySnonC2tl9pU)


### Door sub panel

This panel modifies the module door parameters. It can modify the door size, the width of the frame. It can also change the color of the glass and of the frame. The structure is very similar to the window sub panel module.

![](https://lh5.googleusercontent.com/-io5kzmNbzr0o8jt5NBkJS6ym_auGrFwzWU3o91VkyG7dIPLjYHmztFs_IUhFWmPl3LUOCSyPQAEVEc1GRc6qGCBkTO8bWnqzy-_JB9dTOxeU1slJGbSQaoEst3i57qY9SjqRos)

### Balcony sub panel

This panel controls the balcony module parameters and the outer structure. The windows and the balconies share the same window and frame color for now. The user can decide the width and height of the balcony window. The outer balcony construction parameters that can be modified are the height and depth.

![](https://lh3.googleusercontent.com/3k5g18UCJe09CuS80KPN-SjGg--Gh2ECGj21NfXAKqhuQynq7zDlIYXaB5jYFQ_lVPlaAKHBozMFNEbgZ88uOxqPg1GyjNCcjnjt4TJU1eFegbdiMjhkDQuWjLLcElvZ2Ivw5i8)

## License

MIT License

Copyright (c) [2021] [Alex Morales]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




### License
