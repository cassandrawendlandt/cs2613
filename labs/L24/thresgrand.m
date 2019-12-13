leaf=imread("leaf.jpg");
monoleaf=
ng =
[rows, cols] = threshold(ng, 8 );

clf
hold on;
imshow(leaf);
plot(cols,rows,".","markersize",1);