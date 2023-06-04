# A Brief Talk on Different DNNs in Regulatory Genomics


> In this article, my objective is to compare various well-known deep-learning models utilized in the field of genetics. Additionally, I will elucidate the fundamental design principles behind these models, focusing on their ability to address specific problems.


Convolutional Neural Networks (CNNs) are a type of deep learning model widely employed in image recognition and analysis tasks. Their strength lies in their ability to extract hierarchical representations from input data using convolutional operations and learning feature hierarchies.

In the field of genetics, CNNs have proven valuable for detecting specific motifs or patterns within DNA sequences. They can be specifically designed to identify crucial elements like transcription factor binding sites, promoter regions, or functional segments. Through training on labeled genomic data, CNNs can effectively learn to recognize and classify these patterns, facilitating genome annotation and enhancing our understanding of the functional elements encoded in DNA.

## Simplest CNN model

A simple one CNN layer model typically possesses the following architecture:

- **Input Layer**: The initial input is a DNA sequence. 

- **One-hot Encoding Layer**: The DNA sequence is transformed into a machine-readable format using a technique known as one-hot encoding. This process involves converting the four bases (Adenine (A), Thymine (T), Guanine (G), Cytosine (C)) of the DNA sequence into binary vectors. This transformation is crucial as it allows the model to handle the DNA sequence numerically.

- **Pooling Layer (Pre-CNN)**: Prior to the CNN layers, a pooling layer is employed. The objective of this layer is to down-sample the one-hot encoded input features, thereby reducing the spatial dimensions (height and width), and consequently, the computational complexity. This helps to prevent overfitting by providing an abstracted form of the representation.

- **Convolutional Layers**: The core of the model lies in the CNN layers, which act to extract features from the processed DNA sequences. CNN uses a filter or a kernel that slides over the input data and performs convolution operations, effectively capturing patterns and features within the DNA sequences that might be critical for genetic analysis.

- **Pooling Layer (Post-CNN)**: After the CNN layers, another pooling layer is incorporated. This layer helps in further reducing the dimensionality of the extracted features, focusing on the most important information. By doing this, the model becomes more robust to variations and reduces the risk of overfitting.

| ![](assets/Figure_7.png)|
|:--:|
| <small>Figure 1: Architecture of DeepBind</small>|

## Multi-layer CNNs
However, the use of a single-layer CNN in genetic analysis comes with limitations. Such models struggle to capture the complexity and hierarchical nature of genetic data, often missing out on high-level features and long-range dependencies within the sequences. To address these limitations, the introduction of multiple layers in the CNN architecture proves beneficial. By incorporating multiple layers, the network gains the ability to learn hierarchical representations, effectively capturing both local and global context within the genetic sequences. This multi-layer approach facilitates the extraction of features at different levels and incorporates non-linear activations, enabling the model to comprehend intricate relationships and the complex nature of genetic information.

A typical multi-layer CNN follows a similar structure to the simplest CNN, with the key difference being the stacking of multiple CNN layers. Each layer in the multi-layer CNN performs convolutional operations, extracting local patterns and features from the DNA file. 

| ![](assets/Figure_8.png)|
|:--:|
| <small>Figure 2: Architecture of DeepSEA</small>|

## Add-ons for CNN
Expanding upon the foundation of the simple CNN model, the integration of additional add-on layers offers an opportunity to augment the performance and capabilities of genetic analysis. These supplementary layers, such as Transformers, Residual CNNs, Dilated Residual or Dilated CNNs, attention mechanisms, and Graph Convolutional Networks (GCNs), introduce advanced techniques that extend the model's capacity to capture intricate genetic patterns, long-range dependencies, multi-scale features, and structural relationships. By incorporating these add-on layers, the simple CNN model evolves into a more potent and versatile framework, empowering researchers to delve deeper into the complexities of genetic problems and achieve improved accuracy and efficiency in their analyses.


### Residual CNNs
Residual CNNs, also known as ResNets, were introduced to address the problem of vanishing gradients and facilitate the training of deep networks. In genetics, where the DNA sequences can be extremely long and contain subtle patterns, deep networks can be beneficial. By adding residual connections, which bypass certain convolutional layers, the gradients can flow more easily, enabling better propagation of information throughout the network. This can result in improved feature extraction and better modeling of complex genetic relationships.

| ![](assets/Figure_10.png)|
|:--:|
| <small>Figure 3: Architecture of ExpResNet</small>|

| ![](assets/Figure_11.png)|
|:--:|
| <small>Figure 4: Detail of Residual Module</small>|


### Dilated CNNs
Dilated CNNs, also known as atrous convolution, introduce dilation rates to the convolutional layers. This technique allows the receptive field of the network to grow exponentially without increasing the number of parameters or spatial dimensions. Dilated CNNs have shown promising results in various image analysis tasks, and their application in genetics can be advantageous as well. By using dilated convolutions, the model can capture multi-scale features present in the DNA sequence, which is essential when analyzing genetic data with varying levels of resolution. Combining dilated convolutions with residual connections further enhances the model's capacity to extract meaningful features at different scales.

| ![](assets/Figure_12.png)|
|:--:|
| <small>Figure 5: Architecture of Basenji</small>|

## Treat as Sequential Data
While convolutional neural networks (CNNs) excel at capturing local features in data, they have limitations in learning hidden relationships within sequential data. In contrast, recurrent neural networks (RNNs) and their variants are more powerful tools for processing sequential data. The design of RNNs allows them to capture the time dependencies in data by maintaining an internal state and passing it as input to the next time step.

### LTSM
However, traditional RNNs encounter the vanishing or exploding gradient problem when dealing with long sequences, which makes it challenging to capture long-range dependencies. To overcome this issue, variants such as long short-term memory networks (LSTMs) has been introduced. These network structures incorporate gating mechanisms that effectively control the flow of information, allowing for the capture of long-term dependencies.

| ![](assets/Figure_13.png)|
|:--:|
| <small>Figure 6: Architecture of DeepSite</small>|

Nevertheless, the straightforward approach of stacking CNN and LSTM networks lacks optimization as it fails to fully exploit the strengths inherent in each architecture. To address this limitation, a more enhanced method is proposed in this model. Instead of sequential stacking, the proposed method involves running these two units in parallel, utilizing encoded DNA as the input for both architectures.

| ![](assets/Figure_14.png)|
|:--:|
| <small>Figure 7: Architecture of Deep6mAPred</small>|

### Transformer

In addition to RNNs and their variants, there is a powerful model for handling sequential data called the Transformer. The Transformer is based on self-attention mechanisms, which enable it to establish global dependencies within the sequence. By dynamically attending to different positions in the sequence, the Transformer can efficiently interact and integrate information. This mechanism allows the Transformer to handle longer sequences while maintaining lower computational complexity.

Unlike traditional CNNs that rely on convolutional filters, Transformers utilize a self-attention mechanism to capture dependencies and relationships between DNA sequence elements. This allows the model to effectively learn long-range dependencies, which can be crucial in genetic analysis, where distant regions of DNA may interact or have functional significance. By incorporating Transformer layers into the CNN model, we can potentially improve the model's ability to capture complex genetic patterns and interactions.

| ![](assets/Figure_9.png)|
|:--:|
| <small>Figure 8: Architecture of Enformer</small>|




[^1]: Kelley, David R., Jasper Snoek, and John L. Rinn. “Basset: Learning the Regulatory Code of the Accessible Genome with Deep Convolutional Neural Networks.” Genome Research 26, no. 7 (July 2016): 990–99. https://doi.org/10.1101/gr.200535.115.
