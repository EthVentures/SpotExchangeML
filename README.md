# The Spot Exchange Maching Learning Suite
Welcome to the [Spot Exchange](https://thespot.exchange), a submission to the [Unchain the Frame](https://unchaintheframe.com) Hackathon. Our product ecosystem consists of three main applications linked below:


* Hyperledger based Marketplace [(repo)](https://github.com/EthVentures/SpotExchangeLedger) [(api explorer)](https://api.thespot.exchange:3000/explorer/)
* Mobile Front End [(repo)](https://github.com/EthVentures/SpotExchangeApp) [(demo)](https://thespot.exchange)
* IBM Watson based Price Suggestions [(repo)](https://github.com/EthVentures/SpotExchangeML)


Our project leverages Watson Machine Learning technology to design, build, and deploy custom, online machine learning models. For our Phase II submission, we designed, built, and deployed a machine learning model for one specific business problem that we identified in the marketplace. We also implemented the solution in practice in The Spot Exchange.

## The Business Problem

In a traditional marketplace for renting physical parking spaces, sellers of parking spaces have little direction about how to set prices. In addition, buyers have little direction about whether they are paying a reasonable price for parking. As such, on the seller side, the decision to price parking assets is often made ad hoc without empirical support. On the buyer side, the decision about where to park is influenced by price, but in a suboptimal way.  

## Defining a Machine Learning Problem

In order to develop an influential machine learning solution for the business problem, we first focused on transforming our business problem into a machine learning problem. Machine learning represents computer programs that learn to improve performance at a task through experience. Given this definition, we know that a well-defined machine learning problem consists of a task **T**, a performance measure **P**, and a learning experience **E**. As a result, our machine learning problem can be specified as follows:

  * Task **T**: estimate parking space rental price _r_
  * Performance **P**: _R_<sup>2</sup> (coefficient of determination)
  * Experience **E**: database _D_ of parking reservations with rental prices _r_

From this specification, it’s clear that our objective is to estimate a real-valued target function given a database of parking reservations with observed price signals. The machine learning problem is thus a supervised machine learning problem. There are several approaches  to estimating the target function given our training experience, and each approach has its own advantages and disadvantages. In the next section, we’ll discuss our selected approach.  

## Instance-Based Learning

The nature of our problem lends itself well to an instance-based machine learning solution. Unlike machine learning methods that estimate a generalized target function when training examples are provided, instance-based machine learning methods postpone estimating the target function until specific query instances are available and ready to be estimated. Since the target function is estimated at query time, it is estimated locally for each query instance. In other words, we’re building different approximations of the target function for each query instance. This approach is useful in practice when it’s important to capture local dynamics within irregular decision boundaries, which we find to be true in the parking reservation market.

Within this framework, we specifically leverage k-Nearest-Neighbor regression to estimate the target function. In general, k-Nearest-Neighbor algorithms leverage measures of proximity to identify and retrieve k “neighboring” cases. The k neighboring cases, those that are closest in proximity to our query instance (e.g. in its neighborhood) and thus most “similar” to the query instance, are used to estimate the target function. We leverage the haversine formula to calculate the distance between two instances given by their latitude and longitude. Once the most similar instances have been retrieved, we use local estimation to determine our target.
