import numpy as np
import scipy.stats as stats

def bootstrap(data, n):
    """
    Creates a bootstrap resample - with replacement
    
    Parameters:
    data
    n - sample size
    """
    return np.random.choice(data, size=n, replace=True)



def create_sampling_distribution(data, iterations=30, n=30):
    """
    Creates sampling distribution
    
    Parameters:
    - data: original dataset
    - iterations: number of samples to generate
    - n: size of each sample

    Returns:
    - sampling distribution of sample means
    """
    sampling_dist = []
    for i in range(0,iterations):
        samp = np.random.choice(data, size=n, replace=False)
        sampling_dist.append(np.mean(samp))
    return sampling_dist


def boot_sampling_dist(data, n, iterations):
    """
    Creates a bootstrap resampling distribution.
    
    Parameters:
    - data: original dataset
    - iterations: number of samples to generate
    - n: size of each sample

    Returns:
    - bootstrap sampling distribution of sample means
    """
    samp_dist = []
    for i in range(0,iterations):
        sample = bootstrap(data, n)
        samp_dist.append(np.mean(sample))
    return np.asarray(samp_dist)
        


def welch_t(a, b):
    """
    Calculate Welch's t statistic for two samples
    """
    numerator = np.mean(a) - np.mean(b)
    denominator = np.sqrt(np.var(a, ddof=1)/len(a) + np.var(b, ddof=1)/np.size(b))
    return abs(numerator/denominator)



def welch_df(a, b):
    """ 
    Calculate the effective degrees of freedom for two samples. 
    """
    num = (np.var(a, ddof=1)/np.size(a) + np.var(b, ddof=1)/np.size(b))**2
    denom = (((np.var(a, ddof=1)**2) / (((np.size(a))**2) * (np.size(a)-1)))
             + ((np.var(b, ddof=1)**2) / (((np.size(b))**2) * (np.size(b)-1))))
    return num/denom


def p_value(a, b, two_sided=False):
    """
    Returns the p-value from a Welch's t-test given two datasets (lists, arrays, or series).
    """
    t = welch_t(a,b)
    df = welch_df(a,b)
    p = 1 - stats.t.cdf(t, df)
    if two_sided:
        p += p
    return p


def Cohen_d(group1, group2):
    """Return Cohen's d to evaluate effect size
    Cohen's d = difference between means of two groups 
    divided by their pooled standard deviation
    0.2 = small effect
    0.5 = medium effect
    0.8 large effect
    
    Parameters:
    group1 (array) : series or array
    group2 (array) : series or array
    
    Return:
    d : Cohen's D (Effect Size)
    """
    diff = np.abs(np.mean(group1) - np.mean(group2))
    n1, n2 = len(group1), len(group2)
    var1 = np.var(group1)
    var2 = np.var(group2)
    # Calculate the pooled threshold as shown earlier
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)    
    return d


def remove_outliers(df, col):
    """
    Removes outliers from dataframe column that 
    are more that two standard deviations away 
    from the mean.
    
    Parameters:
    df: datafame
    col: column
    
    Returns:
    dataframe with outliers removed
    """
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound  = q1 - (2 * iqr)
    upper_bound = q3 + (2 * iqr)
    out_df = df.loc[(df[col] > lower_bound) 
                    & (df[col] < upper_bound)]
    return out_df




