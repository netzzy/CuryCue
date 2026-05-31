# Pre-Filling

Pre-Filling is a feature used in a few OPs, like the [Cache TOP](<./Cache_TOP.md> "Cache TOP"), [Cache SOP](<./Cache_SOP.md> "Cache SOP"), and [Texture 3D TOP](<./Texture_3D_TOP.md> "Texture 3D TOP"). It is used to entirely fill up the contents of an OP that usually only fills a portion of it's contents each cook. For example a Cache TOP will normally only cache 1 image per frame. By pre-filling this OP you can cache all of it's images upon load up. 

The pre-fill is done by cooking the node's input(s) at Frame = 1, Frame = 2 etc, up until the number of cooks required to fill up the OP are reached. To generate different information for each cache item, use the expression`me.time.frame`to drive your nodes. For example use`me.time.frame - 1`for the index in the Movie File In TOP (set to Play Mode: Specify Index) to cache the for N images in a Movie File In TOP, into a Cache TOP.
