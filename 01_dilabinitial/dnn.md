# A Brief Talk on Exploring Diverse Deep Neural Networks for DNA Sequence Analysis


> In this talk, I will present a brief overview of popular deep learning models employed in the genetics field, focusing on their architecture. Furthermore, I will delve into the essential design principles that form the foundation of these models. It is crucial for a remarkable model to be intricately woven with the genetic problem it seeks to solve.

## Capture the Pattern within DNA sequences

Over the past few years, Deep Neural Networks (DNNs) have gained significant traction, and been used in various fields. Among the various types of DNN models, the Convolutional Neural Network (CNN) has emerged as a dominant and extensively employed approach. Their exceptional capability stems from their distinctive capacity to extract hierarchical representations from input data, achieved through the utilization of convolutional operations and the learning of feature hierarchies[^1].

In the field of genetics, CNNs have proven valuable for detecting specific motifs or patterns within DNA sequences.[^3] They can be specifically designed to identify crucial elements like transcription factor binding sites, promoter regions, or functional segments.[^4] Through training on labeled genomic data, CNNs can effectively learn to recognize and classify these patterns, facilitating genome annotation and enhancing our understanding of the functional elements encoded in DNA.[^5]

The simplest design of a CNN model typically follows the following architecture:


- **Input Layer**: The initial input is a DNA sequence. 

- **One-hot Encoding Layer**: The DNA sequence is transformed into a machine-readable format using a technique known as one-hot encoding. This process involves converting the four bases (Adenine (A), Thymine (T), Guanine (G), Cytosine (C)) of the DNA sequence into binary vectors. This transformation is crucial as it allows the model to handle the DNA sequence numerically.

- **Pooling Layer (Pre-CNN)**: Prior to the CNN layers, a pooling layer is employed. The objective of this layer is to down-sample the one-hot encoded input features. This helps to prevent overfitting by providing an abstracted form of the representation.

- **Convolutional Layers**: The core of the model lies in the CNN layers, which act to extract features from the processed DNA sequences. CNN uses a filter or a kernel that slides over the input data and performs convolution operations, effectively capturing patterns and features within the DNA sequences that might be critical for genetic analysis.

- **Pooling Layer (Post-CNN)**: After the CNN layers, another pooling layer is incorporated. This layer helps in further reducing the dimensionality of the extracted features, focusing on the most important information. 

| ![](assets/Figure_7.png)|
|:--:|
| <small>Figure 1: Architecture of DeepBind [^5]</small>|

DeepBind was created by Babak Alipanahi et al. to tackle the challenge of deciphering the sequence specificities of DNA- and RNA-binding proteins.[^6] Through the use of convolutional neural networks (CNNs), DeepBind exhibits an impressive capability to detect and comprehend the localized patterns and interdependencies found within biological sequences. 

## Capture More Complex Features
The utilization of a single-layer CNN in analysis encounters certain limitations. These models face challenges in comprehending the intricate nature and hierarchical structure of complex data, leading to potential oversights of high-level features and long-range dependencies within the sequences.[^7] Similar challenges are expected to arise in the field of Regulatory Genomics.

To address these limitations, the incorporation of multiple layers into the CNN architecture is highly beneficial. By integrating multiple layers, the network gains the capability to acquire hierarchical representations, thereby facilitating the effective capture of both local and global context within the genetic sequences.[^8] This multi-layer approach significantly enhances the model's ability to comprehend the intricate relationships and intricate patterns that are inherent in the data, aligning well with the complex nature of DNA sequences.

A typical multi-layer CNN follows a similar structure to the simplest CNN, with the key difference being the stacking of multiple CNN layers. Each layer in the multi-layer CNN performs convolutional operations, extracting local patterns and features from the DNA file. 

| ![](assets/Figure_8.png)|
|:--:|
| <small>Figure 2: Architecture of DeepSEA [^9]</small>|

The problem that Jian Zhou and Olga G Troyanskaya want to solve with DeepSEA is the identification and prediction of the functional effects of noncoding variants in the genome.[^9] DeepSEA surpasses DeepBind by directly predicting the functional effects of noncoding variants based on genomic sequence. It offers single-nucleotide sensitivity in predicting various chromatin features. The multi-layer structure in DeepSEA allows the model to capture sequence dependencies at multiple spatial scales. By integrating sequence information from a wide sequence context, DeepSEA considers the surrounding DNA sequence of the variant position, which is crucial for understanding its functional effects.

## Add-ons for CNN
Expanding upon the foundation of the simple CNN model, the integration of additional add-on layers offers an opportunity to augment the performance and capabilities of genetic analysis. These supplementary layers, such as Residual CNNs, Dilated Residual or Dilated CNNs introduce advanced techniques that extend the model's capacity to capture intricate genetic patterns, long-range dependencies, multi-scale features, and structural relationships. By incorporating these add-on layers, the simple CNN model evolves into a more potent and versatile framework, empowering researchers to delve deeper into the complexities of genetic problems and achieve improved accuracy and efficiency in their analyses.

### Residual CNNs
Residual CNNs, also known as ResNets, were introduced to address the problem of vanishing gradients and facilitate the training of deep networks.[^11] The key idea behind residual units or ResNet is the incorporation of "shortcut connections" or "skip connections".[^12] These connections enable the gradient to be backpropagated directly to earlier layers of the CNN, which significantly facilitates the training process. This can result in improved feature extraction and better modeling of complex genetic relationships. 

| ![](assets/Figure_10.png)|
|:--:|
| <small>Figure 3: Architecture of ExpResNet[^10]</small>|

| ![](assets/Figure_11.png)|
|:--:|
| <small>Figure 4: Detail of Residual Module[^10]</small>|

Yilun Zhang et al. aim to devise a method for predicting gene expression levels directly from DNA sequences by deploying the ExpResNet model.[^10] Regular approaches like multi-layer convolutional neural networks (CNNs) for this prediction task often pose challenges during training, and increasing the number of layers does not necessarily enhance their performance. To circumvent these limitations, Zhang et al. suggest the use of a deep residual network, or ResNet, for direct prediction of gene expression levels from DNA sequences.

### Dilated CNNs
Dilated CNNs, also known as atrous convolution, introduce dilation rates to the convolutional layers. This technique allows the receptive field of the network to grow exponentially without increasing the number of parameters or spatial dimensions.[^13] Dilated CNNs have shown promising results in various image analysis tasks, and their application in genetics can be advantageous as well. By using dilated convolutions, the model can capture multi-scale features present in the DNA sequence, which is essential when analyzing genetic data with varying levels of resolution.[^14]

| ![](assets/Figure_12.png)|
|:--:|
| <small>Figure 5: Architecture of Basenji</small> [^15]|

Kelley et al. aim to develop a model, named Basenji, for predicting cell-type-specific epigenetic and transcriptional profiles directly from DNA sequences by employing Dilated Convolutional Neural Networks (CNNs). Traditional approaches like multi-layer convolutional neural networks for this prediction task often present difficulties during training, and incrementing the number of layers does not necessarily improve their performance. To overcome these challenges, Kelley and colleagues suggest the use of Dilated CNNs for direct prediction of cell-type-specific epigenetic and transcriptional profiles from DNA sequences.[^15]


## Capture Long-term Dependencies within DNA sequences
While convolutional neural networks (CNNs) excel at capturing local features in data, they have limitations in learning hidden relationships within sequential data. In contrast, recurrent neural networks (RNNs) and their variants are more powerful tools for processing sequential data.[^16] The design of RNNs allows them to capture the time dependencies in data by maintaining an internal state and passing it as input to the next time step.



### LSTM
However, traditional RNNs encounter the vanishing or exploding gradient problem when dealing with long sequences, which makes it challenging to capture long-range dependencies. To overcome this issue, variants such as long short-term memory networks (LSTMs) has been introduced.[^17] These network structures incorporate gating mechanisms that effectively control the flow of information, allowing for the capture of long-term dependencies.

| ![](assets/Figure_13.png)|
|:--:|
| <small>Figure 6: Architecture of DeepSite [^18]</small>|

Yongqing Zhang et al. aim to address the challenge of predicting DNA–protein binding sites directly from DNA sequences by utilizing a combination of bidirectional Long Short-Term Memory (BLSTM) and Convolutional Neural Networks (CNNs), which they have named "DeepSite". Traditional methods like multi-layer CNNs for this task have been found to lack the necessary precision and cannot adequately represent the dependency information of DNA sequence within the CNN framework. To address these issues, the team incorporates a Bi-LSTM layer along with the traditional CNN structure. This combination allows DeepSite to capture long-term dependencies between the sequence motifs in DNA, enhancing its predictive performance significantly.[^18]

However, the conventional approach of simply stacking CNN and LSTM networks lacks optimization as it fails to fully leverage the inherent strengths of each architecture.[^19] To overcome this limitation, a more advanced method is proposed in this model. Instead of sequential stacking, the proposed approach involves running these two components in parallel. This is because CNNs excel at extracting spatial and local features through convolution operations and pooling layers, while LSTMs are adept at capturing long-term dependencies in sequential data due to their gating mechanisms. By employing parallel processing, we can simultaneously utilize the spatial-feature extraction capability of CNNs and the long-term dependency capturing ability of LSTMs, resulting in a more comprehensive representation of the data.
| ![](assets/Figure_14.png)|
|:--:|
| <small>Figure 7: Architecture of Deep6mAPred [^20]</small>|

Xingyu Tang et al. constructed a deep learning method for predicting DNA N6-methyladenine sites, which is applicable across plant species, called Deep6mAPred. The core of the method is a deep neural network that uses both Convolutional Neural Networks (CNN) and Bi-directional Long Short-Term Memory (Bi-LSTM) in parallel rather than in a series connection. This structure enables the model to leverage the strengths of both CNN and LSTM. [^20]



### Transformer

In addition to RNNs and their variants, there is a powerful model for handling sequential data called the Transformer.[^21] The Transformer is based on self-attention mechanisms, which enable it to establish global dependencies within the sequence. By dynamically attending to different positions in the sequence, the Transformer can efficiently interact and integrate information. This mechanism allows the Transformer to handle longer sequences while maintaining lower computational complexity.[^22]

Unlike traditional CNNs that rely on convolutional filters, Transformers utilize a self-attention mechanism to capture dependencies and relationships between DNA sequence elements. This allows the model to effectively learn long-range dependencies, which can be crucial in genetic analysis, where distant regions of DNA may interact or have functional significance. By incorporating Transformer layers into the CNN model, we can potentially improve the model's ability to capture complex genetic patterns and interactions.[^23]

| ![](assets/Figure_9.png)|
|:--:|
| <small>Figure 8: Architecture of Enformer[^24]</small>|

Žiga Avsec and his team have successfully developed Enformer, a deep learning model specifically designed to enhance the accuracy of gene expression prediction from DNA sequences. The unique self-attention mechanism of Transformers makes them particularly well-suited for this task. By considering the relationship between each position in the input sequence and all other positions, the model gains valuable insights.[^24]

## Summary
When designing a Deep Neural Network (DNN) for genetic problems, it is crucial to adopt a meticulous approach that enables the model to effectively comprehend and interpret the intricate nature of genetic data. A key aspect of this process involves capturing inherent patterns present within DNA sequences. The Convolutional Neural Network (CNN) has gained recognition as a valuable tool in this domain due to its ability to extract hierarchical representations.

In genetic problem-solving, a remarkable deep neural network (DNN) model needs to be intricately woven with the problem it aims to address due to the complexity and multi-faceted nature of genetic data. DNA sequences contain intricate relationships, patterns, and dependencies that require sophisticated and specialized algorithms to decipher accurately. 

Designing a DNN model to fit the unique structure and characteristics of genetic data allows the model to capture these inherent complexities more effectively. For instance, multi-layer CNNs can extract local and global patterns in the DNA sequences, which are critical for understanding functional elements encoded in DNA. Advanced layers like Residual CNNs, Dilated CNNs, and Transformers enable the model to navigate challenges such as vanishing gradients, multi-scale feature extraction, and long-range dependencies.

Furthermore, each genetic problem possesses unique characteristics, and an effective model should consider these idiosyncrasies during its design. Some tasks may involve the prediction of specific features in a sequence, while others might need to consider the entire sequence context. Tailoring the model to the specific requirements of the problem helps ensure it can capture the most relevant and critical information, thereby improving its predictive power and accuracy. 

In summary, a remarkable model must be intricately woven with the genetic problem to ensure that it's capable of understanding and interpreting the data in a way that addresses the problem's inherent complexity and uniqueness. This alignment between the model and the problem leads to improved performance and more accurate, meaningful results.


[^1]: Kelley, David R., Jasper Snoek, and John L. Rinn. “Basset: Learning the Regulatory Code of the Accessible Genome with Deep Convolutional Neural Networks.” Genome Research 26, no. 7 (July 2016): 990–99. https://doi.org/10.1101/gr.200535.115.

[^2]: Alzubaidi, Laith, Jinglan Zhang, Amjad J. Humaidi, Ayad Al-Dujaili, Ye Duan, Omran Al-Shamma, J. Santamaría, Mohammed A. Fadhel, Muthana Al-Amidie, and Laith Farhan. “Review of Deep Learning: Concepts, CNN Architectures, Challenges, Applications, Future Directions.” Journal of Big Data 8, no. 1 (March 31, 2021): 53. https://doi.org/10.1186/s40537-021-00444-8.

[^3]: Wu, Di, Deepti S. Karhade, Malvika Pillai, Min-Zhi Jiang, Le Huang, Gang Li, Hunyong Cho, Jeff Roach, Yun Li, and Kimon Divaris. “Machine Learning and Deep Learning in Genetics and Genomics.” In Machine Learning in Dentistry, edited by Ching-Chang Ko, Dinggang Shen, and Li Wang, 163–81. Cham: Springer International Publishing, 2021. https://doi.org/10.1007/978-3-030-71881-7_13.

[^4]: Alipanahi, Babak, Andrew Delong, Matthew T. Weirauch, and Brendan J. Frey. “Predicting the Sequence Specificities of DNA- and RNA-Binding Proteins by Deep Learning.” Nature Biotechnology 33, no. 8 (August 2015): 831–38. https://doi.org/10.1038/nbt.3300.

[^5]: Hu, Xuehai, Alisdair R Fernie, and Jianbing Yan. “Deep Learning in Regulatory Genomics: From Identification to Design.” Current Opinion in Biotechnology 79 (February 1, 2023): 102887. https://doi.org/10.1016/j.copbio.2022.102887.

[^6]: Alipanahi, Babak, Andrew Delong, Matthew T. Weirauch, and Brendan J. Frey. “Predicting the Sequence Specificities of DNA- and RNA-Binding Proteins by Deep Learning.” Nature Biotechnology 33, no. 8 (August 2015): 831–38. https://doi.org/10.1038/nbt.3300.

[^7]: Yu, Wei, Kuiyuan Yang, Hongxun Yao, Xiaoshuai Sun, and Pengfei Xu. “Exploiting the Complementary Strengths of Multi-Layer CNN Features for Image Retrieval.” Neurocomputing 237 (May 10, 2017): 235–41. https://doi.org/10.1016/j.neucom.2016.12.002.

[^8]: Kulkarni, Praveen, Joaquin Zepeda, Frederic Jurie, Patrick Perez, and Louis Chevallier. “Hybrid Multi-Layer Deep CNN/Aggregator Feature for Image Classification.” In 2015 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 1379–83, 2015. https://doi.org/10.1109/ICASSP.2015.7178196.

[^9]: Zhou, Jian, and Olga G. Troyanskaya. “Predicting Effects of Noncoding Variants with Deep Learning–Based Sequence Model.” Nature Methods 12, no. 10 (October 2015): 931–34. https://doi.org/10.1038/nmeth.3547.

[^10]: Zhang, Yilun, Xin Zhou, and Xiaodong Cai. “Predicting Gene Expression from DNA Sequence Using Residual Neural Network.” bioRxiv, July 23, 2020. https://doi.org/10.1101/2020.06.21.163956.

[^11]: Targ, Sasha, Diogo Almeida, and Kevin Lyman. “Resnet in Resnet: Generalizing Residual Architectures.” arXiv, March 25, 2016. https://doi.org/10.48550/arXiv.1603.08029.

[^12]: He, Kaiming, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. “Deep Residual Learning for Image Recognition,” 770–78, 2016. https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html.

[^13]: Lei, Xinyu, Hongguang Pan, and Xiangdong Huang. “A Dilated CNN Model for Image Classification.” IEEE Access 7 (2019): 124087–95. https://doi.org/10.1109/ACCESS.2019.2927169.

[^14]: Karbalayghareh, Alireza, Merve Sahin, and Christina S. Leslie. “Chromatin Interaction–Aware Gene Regulatory Modeling with Graph Attention Networks.” Genome Research 32, no. 5 (May 1, 2022): 930–44. https://doi.org/10.1101/gr.275870.121.

[^15]: “Sequential Regulatory Activity Prediction across Chromosomes with Convolutional Neural Networks.” Accessed June 7, 2023. https://genome.cshlp.org/content/28/5/739.full.

[^16]: Yin, Wenpeng, Katharina Kann, Mo Yu, and Hinrich Schütze. “Comparative Study of CNN and RNN for Natural Language Processing.” arXiv, February 7, 2017. https://doi.org/10.48550/arXiv.1702.01923.

[^17]: Uddin, Md Azher, Joolekha Bibi Joolee, and Young-Koo Lee. “Depression Level Prediction Using Deep Spatiotemporal Features and Multilayer Bi-LTSM.” IEEE Transactions on Affective Computing 13, no. 2 (April 2022): 864–70. https://doi.org/10.1109/TAFFC.2020.2970418.

[^18]: Zhang, Yongqing, Shaojie Qiao, Shengjie Ji, and Yizhou Li. “DeepSite: Bidirectional LSTM and CNN Models for Predicting DNA–Protein Binding.” International Journal of Machine Learning and Cybernetics 11, no. 4 (April 1, 2020): 841–51. https://doi.org/10.1007/s13042-019-00990-x.

[^19]: Heryadi, Yaya, and Harco Leslie Hendric Spits Warnars. “Learning Temporal Representation of Transaction Amount for Fraudulent Transaction Recognition Using CNN, Stacked LSTM, and CNN-LSTM.” In 2017 IEEE International Conference on Cybernetics and Computational Intelligence (CyberneticsCom), 84–89, 2017. https://doi.org/10.1109/CYBERNETICSCOM.2017.8311689.

[^20]: Tang, Xingyu, Peijie Zheng, Xueyong Li, Hongyan Wu, Dong-Qing Wei, Yuewu Liu, and Guohua Huang. “Deep6mAPred: A CNN and Bi-LSTM-Based Deep Learning Method for Predicting DNA N6-Methyladenosine Sites across Plant Species.” Methods 204 (August 1, 2022): 142–50. https://doi.org/10.1016/j.ymeth.2022.04.011.

[^21]: Han, Kai, An Xiao, Enhua Wu, Jianyuan Guo, Chunjing XU, and Yunhe Wang. “Transformer in Transformer.” In Advances in Neural Information Processing Systems, 34:15908–19. Curran Associates, Inc., 2021. https://proceedings.neurips.cc/paper/2021/hash/854d9fca60b4bd07f9bb215d59ef5561-Abstract.html.

[^22]: Zhao, Yucheng, Guangting Wang, Chuanxin Tang, Chong Luo, Wenjun Zeng, and Zheng-Jun Zha. “A Battle of Network Structures: An Empirical Study of CNN, Transformer, and MLP.” arXiv, November 25, 2021. https://doi.org/10.48550/arXiv.2108.13002.

[^23]: Zhang, Xiaodan, Jinxiang Xuan, Chensong Yao, Qijuan Gao, Lianglong Wang, Xiu Jin, and Shaowen Li. “A Deep Learning Approach for Orphan Gene Identification in Moso Bamboo (Phyllostachys Edulis) Based on the CNN + Transformer Model.” BMC Bioinformatics 23, no. 1 (May 5, 2022): 162. https://doi.org/10.1186/s12859-022-04702-1.

[^24]: “Effective Gene Expression Prediction from Sequence by Integrating Long-Range Interactions | Nature Methods.” Accessed June 7, 2023. https://www.nature.com/articles/s41592-021-01252-x.
