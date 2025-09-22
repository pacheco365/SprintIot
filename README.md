# Aplicação de Reconhecimento Facial Local

## Objetivo
Desenvolver uma aplicação para reconhecimento de faces.

## Instruções de Execução
1. Instale dependências: `pip install opencv-contrib-python numpy`.
2. Rode `python train.py` para capturar imagens e treinar.
3. Rode `python recognize.py` para reconhecimento em tempo real.

## Dependências
- Python 3.8+
- opencv-contrib-python
- numpy

## Parâmetros Ajustáveis
- Detecção (recognize.py):
  - scaleFactor: 1.1 (ajuste para sensibilidade a tamanhos de face).
  - minNeighbors: 5 (ajuste para rigor na confirmação de faces).
- Reconhecimento (train.py):
  - radius: 1 (tamanho do padrão local).
  - neighbors: 8 (sensibilidade a variações).
- Impacto: Ajuste valores, re-execute e observe mudanças em detecções/precisão.

## Nota Ética sobre Uso de Dados Faciais
Dados faciais são sensíveis e envolvem privacidade. Esta aplicação armazena imagens localmente, mas em usos reais: obtenha consentimento explícito, evite armazenamento desnecessário, não compartilhe dados sem permissão e considere regulamentações como LGPD/GDPR. Limitações incluem viés em diversidade étnica; teste com variados grupos para equidade.

## Limitações e Próximos Passos
Limitações: Sensível a iluminação/ângulos, não lida com múltiplos usuários bem. Próximos: Integrar deep learning (ex: FaceNet), adicionar landmarks com dlib, melhorar ética com criptografia de dados.

## Integrantes
-Anna Yagyu 〡 Rm 550360 
-Breno Silva 〡 Rm 99275 
-Danilo Urze 〡 Rm 99465 
-Gabriel Pacheco 〡Rm550191

## Vídeo
https://youtu.be/dbOOuLj6vjQ
