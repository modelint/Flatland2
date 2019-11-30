# Flatland2

This is a recent project as of November 2019 to create a markup language and diagram layout engine for a limited range of model diagrams. The primary motivation for this effort is to mimimize and hopefully eliminate the time wasting activity of pixel pushing diagram elements. It would also be nice to store all model information, including graphical layout cues, in a text from for each configuration management.

If you get you hands on a copy of our book [Models to Code](https://www.modelstocode.com) you will see that we use an open source tool chain to get from models all the way to efficient, high-performance C code. This program is one step in that tool chain. It will input a file containing the Executable UML models in text form, filter out the diagram layout markup and diagram content, and then output a high quality PDF (or some other selected output format) for each supported diagram type.

At present, supported diagram types are: class, state, collaboration and domain diagrams. Seqeunce diagrams are not supported, but the PlantUML output for sequence diagrams, with a bit of tweaking already looks pretty good.

Why not just use PlantUML for everything? Simple: The layout sucks for the kinds of diagrams we do. If you just want to plop a handful of elements down on a page for documentation purposes, PlantUML is fine. But, if you have a serious quantity of grahical model content, as we do, that serves as input to a serious code generation pipeline, as we do, PlantUML, and any open source diagram layout tool chain that we are aware of, just doesn't deliver. There is simply no adequate control of the layout which is so important for making diagrams clear and understandable (which is kind of the whole point of modeling anyway, right?). And from many of the comments we've seen from the developers, it appears that control over layout will never be a priority since the whole philosophy is to free you from thinking about layout.

Our philosophy, by contrast, is to lay the models out strategically so that you can tackle the modeled subject matter complexity and leave behind a useful trail of helpful and maintainable documentation.

We're in the early phases of development, so there is NOTHING here for you to use yet, but feel free to browse the code. We'll make a big announcement when it's ready for public consumption sometime in 2020.

At present I am writing all the code in Python 3.7 using pycairo for the layout. This is my first Python 3 project and I spend most of my time analyzing systems and building executable UML models at the Toyota Research Institute and for other clients, so don't be too surprised if it looks a bit like amateur hour in the code files here. Nonetheless, I intend to get this thing working ASAP so that I don't have to push model pixels ever again!  / Leon Starr
