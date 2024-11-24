
# 🥏 Cálculo de Movimento Balístico

Este repositório contém um código desenvolvido em Python para o cálculo de diversos parâmetros relacionados ao movimento balístico, utilizado em um trabalho de Física na faculdade. O programa realiza cálculos a partir de valores de entrada fornecidos pelo usuário, como posição inicial, velocidade inicial, ângulo de lançamento, e tempo de observação.

## ⚙️ Funcionalidades

O programa calcula:

1. **Velocidades iniciais nas direções x e y**: Com base na velocidade inicial e no ângulo de lançamento.
2. **Tempo de queda**: O tempo que o objeto leva para atingir a altura final.
3. **Alcance horizontal (distância máxima)**: A distância percorrida no eixo horizontal antes de atingir o solo.
4. **Altura máxima**: O ponto mais alto atingido durante o movimento.
5. **Velocidade na altura máxima**: A magnitude da velocidade no ponto mais alto do trajeto.
6. **Velocidade no ponto de chegada**: A velocidade do objeto ao atingir o solo (incluindo componentes x e y).
7. **Coordenadas no instante especificado**: A posição do objeto no instante de tempo fornecido.
8. **Velocidade no instante especificado**: A velocidade do objeto em um determinado instante de tempo.

## ⌨️ Estrutura do Código

O código segue os seguintes passos:
1. Solicita dados de entrada do usuário:
   - Posição inicial
   - Altura final
   - Velocidade inicial
   - Ângulo de lançamento (em graus)
   - Instante de tempo
2. Realiza cálculos usando as fórmulas da cinemática e da gravidade (9.81 m/s²).
3. Apresenta os resultados detalhados.

## 🎲 Entrada de Dados

Os valores de entrada devem ser fornecidos pelo usuário no início do programa:
- **Posição inicial (m)**: Altura inicial do objeto.
- **Altura final (m)**: Altura onde o objeto atinge o solo.
- **Velocidade inicial (m/s)**: Velocidade de lançamento.
- **Ângulo de lançamento (graus)**: Ângulo em relação ao plano horizontal.
- **Instante de tempo (s)**: Momento no qual se deseja calcular a posição e velocidade do objeto.

## 📤 Saída de Dados

O programa retorna:
- Componentes das velocidades iniciais nas direções x e y.
- Tempo de queda, alcance horizontal e altura máxima.
- Velocidade (e suas componentes) em diferentes momentos do movimento.
- Coordenadas do objeto no instante especificado.

## 🔩 Requisitos

- Python 3.6 ou superior.
- Biblioteca `math` (padrão do Python).

## 💻 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/movimento-balistico.git
   ```
2. Navegue até a pasta do projeto:
   ```bash
   cd movimento-balistico
   ```
3. Execute o programa:
   ```bash
   python movimento_balistico.py
   ```

## 👥 Parceria

Código feito em parceria com o Nathan ⮧ <br>
[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/Neromakii
) 


---

**Nota:** Este código foi desenvolvido como parte de um projeto acadêmico e não é destinado para aplicações de alta precisão.
