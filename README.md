# whale4kaggle

Trying some ideas for whale Competition

https://www.kaggle.com/c/humpback-whale-identification

download train & test images from competition


generate - inputGeneratedPerImage folder for generating Ids wise whales..

Subject Ideas for myself

Theory - http://www.alaskahumpbacks.org/matching.html

idea - https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78 ->step2


What I want to do (steps for whale competition) :

Train:
  1. Segmentation of whale tail find. with fixed size about 200*200(some fixed size)
  2. then manual annotation on some images with 50 landmark points.. may be on 200 images..
  3. Create keras model to detect landmark points on other images now...
  4. generate embedding by these generated landmarks for all Ids..
  5. Create a model for finding correct Ids by new images

Test :
  new image -> model -> generate 128 measurements(embedding) -> compare with another model for close to any Ids saved already...
