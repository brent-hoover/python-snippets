"""
Title: Matlab-like 'spy' and 'pcolor' functions
Submitter: Rick Muller (other recipes)
Last Updated: 2005/03/02
Version no: 1.0
Category: Image
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/390208

Description:

I really like the 'spy' and 'pcolor' functions, which are useful in
viewing matrices. 'spy' prints colored blocks for values that are above
a threshold, and 'pcolor' prints out each element in a continuous range
of colors.  The attached is a little Python/PIL script that does these
functions for Numpy arrays.
"""

def spy_matrix_pil(A,fname='tmp.png',cutoff=0.1,do_outline=0,
                   height=300,width=300):
    """\
    Use a matlab-like 'spy' function to display the large elements
    of a matrix using the Python Imaging Library.

    Arguments:
    A          Input Numpy matrix
    fname      Output filename to which to dump the graphics (default 'tmp.png')
    cutoff     Threshold value for printing an element (default 0.1)
    do_outline Whether or not to print an outline around the block (default 0)
    height     The height of the image (default 300)
    width      The width of the image (default 300)

    Example:
    >>> from Numeric import identity,Float
    >>> a = identity(10,Float)
    >>> spy_matrix_pil(a)
    
    """
    import Image,ImageDraw
    img = Image.new("RGB",(width,height),(255,255,255))
    draw = ImageDraw.Draw(img)
    n,m = A.shape
    if n>width or m>height:
        raise "Rectangle too big %d %d %d %d" % (n,m,width,height)
    for i in range(n):
        xmin = width*i/float(n)
        xmax = width*(i+1)/float(n)
        for j in range(m):
            ymin = height*j/float(m)
            ymax = height*(j+1)/float(m)
            if abs(A[i,j]) > cutoff:
                if do_outline:
                    draw.rectangle((xmin,ymin,xmax,ymax),fill=(0,0,255),
                                        outline=(0,0,0))
                else:
                    draw.rectangle((xmin,ymin,xmax,ymax),fill=(0,0,255))
    img.save(fname)
    return

def get_color(a,cmin,cmax):
    """\
    Convert a float value to one of a continuous range of colors.
    Rewritten to use recipe 9.10 from the Python Cookbook.
    """
    import math
    try: a = float(a-cmin)/(cmax-cmin)
    except ZeroDivisionError: a=0.5 # cmax == cmin
    blue = min((max((4*(0.75-a),0.)),1.))
    red = min((max((4*(a-0.25),0.)),1.))
    green = min((max((4*math.fabs(a-0.5)-1.,0)),1.))
    return '#%1x%1x%1x' % (int(15*red),int(15*green),int(15*blue))

def get_color_grey(a,cmin,cmax):
    """\
    Convert a float value to one of a continuous range of colors.
    Rewritten to use recipe 9.10 from the Python Cookbook.
    """
    import math
    try: a = float(a-cmin)/(cmax-cmin)
    except ZeroDivisionError: a=0.5 # cmax == cmin
    return '#%02x%02x%02x' % (int(255*a),int(255*a),int(255*a))

def pcolor_matrix_pil(A, fname='tmp.png', do_outline=0,
                      height=300, width=300, colorfunc=get_color_grey,
                      value_range=None):
    """\
    Use a matlab-like 'pcolor' function to display the large elements
    of a matrix using the Python Imaging Library.

    Arguments:
    A          Input Numpy matrix
    fname      Output filename to which to dump the graphics (default 'tmp.png')
    do_outline Whether or not to print an outline around the block (default 0)
    height     The height of the image (default 300)
    width      The width of the image (default 300)

    Example:
    >>> from Numeric import identity,Float
    >>> a = identity(10,Float)
    >>> pcolor_matrix_pil(a)
    
    """
    import Image,ImageDraw
    img = Image.new("RGB",(width,height),(255,255,255))
    draw = ImageDraw.Draw(img)

    n,m = A.shape
    # this apparently doesn't work with new numpy, for loops added --dmcc
    # mina = min(min(A))
    # maxa = max(max(A))
    if value_range is not None:
        mina, maxa = value_range
    else:
        mina = A[0,0]
        maxa = A[0,0]
        for i in range(n):
            for j in range(m):
                mina = min(A[i,j], mina)
                maxa = max(A[i,j], maxa)

    if n>width or m>height:
        raise "Rectangle too big %d %d %d %d" % (n,m,width,height)
    for i in range(n):
        xmin = width*i/float(n)
        xmax = width*(i+1)/float(n)
        for j in range(m):
            ymin = height*j/float(m)
            ymax = height*(j+1)/float(m)
            color = colorfunc(A[i,j],mina,maxa)
            if do_outline:
                draw.rectangle((xmin,ymin,xmax,ymax),fill=color,
                               outline=(0,0,0))
            else:
                draw.rectangle((xmin,ymin,xmax,ymax),fill=color)
                    
    img.save(fname)
    return

if __name__ == "__main__":
    from Numeric import identity, Float

    a = identity(10,Float)
    spy_matrix_pil(a)
    pcolor_matrix_pil(a,'tmp2.png')
