leaf=imread("leaf.jpg");
monoleaf=monochrome(leaf);
smoothed= smooth(monoleaf,4);
ng = normgrad(smoothed);
[rows, cols] = threshold(ng,7);

clf
hold on;
imshow(leaf,[]);
plot(cols,rows,".","markersize",1);