pdf("plotting.pdf")
x <- 1:5    #create vector 1,2,3,4,5
y <- x^2    # square each value of x
plot(x,y, type = "b", col = "blue", main = "Base R Plot")
# type=b means both line and point, col=blue means point/line color is blue and main adds a plot title