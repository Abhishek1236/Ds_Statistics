import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials

    """

    def __init__(self, prob=.5, size=20):

        Distribution.__init__(self)
        self.p = prob
        self.n = size

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """

        mean = (self.n)*(self.p)
        self.mean = mean
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """

        stdev = math.sqrt((self.n)*(self.p)*(1-self.p))
        self.stdev = stdev
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        self.p = ((self.data).count(1))/(self.n)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        x = ['0', '1']
        y = [(self.data).count(0), (self.data).count(1)]
        plt.bar(x, y)
        plt.xlabel('Outcomes')
        plt.ylabel('Count')
        plt.title('Binomial distribution chart')
       
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

     

        first_part = (math.factorial(self.n)/(math.factorial(k) * math.factorial(self.n - k)))
        second_part = ((self.p) ** k)*((1-self.p)**(self.n - k))
        pdf = first_part * second_part
        return pdf

    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

     

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(self.n):
            x.append(i)
            y.append(self.pdf(i))
        plt.bar(x, y)
        plt.xlabel('Count')
        plt.ylabel('Pdf')
        plt.title('Binomial distribution chart')
        return x, y

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        result.mean = (result.p)*(result.n)
        result.stdev = math.sqrt(result.n * result.p * (1 - result.p))

        return result

 

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
