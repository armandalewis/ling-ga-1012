## General model
- exact match accuracy (multi-class)
- mean area under the receiver operating characteristic (ROC) curve score
- mean precision
- mean recall
- mean F1 score


| Task  | Metric                       |
|-------|------------------------------|
| CoLA  | Matthew's corr               |
| STS-B | Person/Spearman corr.        |
| WiC   | Accuracy                     |
| RTE   | Accuracy                     |
| WinoG  | Gender Parity / Accuracy    |

## Autoregressive Model: GPT-2
Autoregressive models rely on the decoder part of the original transformer and use an attention mask so that at each position, the model can only look at the tokens before the attention heads. See https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

Enhanced from GPT: allows for language modeling and multitask language modeling/multiple choice classification.
- add perplexity

## Autoencoder Model: BERT
Autoencoder models rely on the encoder part of the original transformer and use no mask so the model can look at all the tokens in the attention heads. See https://arxiv.org/abs/1810.04805

From Hugging Face, library for sentence classification and multiple choice classification.  Can integrate off-the-shelf or custom eval metrics. See WEAT code for bias analysis.

