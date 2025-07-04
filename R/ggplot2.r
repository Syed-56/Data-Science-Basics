library(ggplot2)  #import library

df <- data.frame(x=1:5, y=c(1,4,9,16,25))  #creates data frame with x & y columns

p <- ggplot(df, aes(x,y)) + geom_line() + geom_point() +
  ggtitle("Quadratic Plot") +
  labs(x = "X-Axis", y = "Y-Axis")
# df, aes(x,y) means df as data source and maping x to x-axis and y to y-axis
# geom_line() add line plot and geom_point() adds point on same plot

pdf("ggplot2.r.pdf")     # Start writing to PDF
print(p)              # Explicitly print the ggplot object to write it
dev.off()             # Close the PDF file