# 🛡️ Defensor da Muralha - v2.0.0

Um jogo de defesa estilo tower defense desenvolvido em Python com PyGame. Defenda sua muralha contra inimigos cada vez mais fortes!

## Sobre o Jogo

**Defensor da Muralha** é um jogo de defesa onde você controla um soldado que deve proteger uma muralha contra hordas de inimigos. O objetivo é sobreviver o máximo de tempo possível enquanto elimina o maior número de inimigos.

### Mecânicas Principais
- **Controle do soldado**: Movimente-se pela tela para posicionar-se estrategicamente
- **Dois tipos de tiros**: Tiro rápido (fraco) e tiro lento (forte)
- **Sistema de HP**: Você e a muralha têm pontos de vida separados
- **Inimigos variados**: Três tipos diferentes de inimigos com habilidades distintas
- **Sistema de pontuação**: Registro de melhores tempos e maior número de kills
- **Recuperação de HP**: A cada 15 inimigos mortos, recupera 1 HP

## Arquitetura do Projeto (v2.0.0)

A versão 2.0.0 é uma refatoração completa do código original, com melhorias significativas:

### Melhorias da v2.0.0
1. **Organização por responsabilidades**: Código dividido em módulos especializados
2. **Herança e reuso**: Sistema de entidades com classe base `Entity`
3. **Gerenciamento de áudio centralizado**: Classe `AudioManager` para controle de sons
4. **Sistema de records criptografado**: Pontuações salvas com criptografia Fernet
5. **Menu interativo**: Sistema de navegação com animações
6. **Código mais limpo**: Nomeclatura em português e padrões consistentes

## Objetivo do Jogo

Proteja a muralha contra os inimigos que vêm do topo da tela. Você perde se:
1. Seu HP chegar a 0 (soldado morre)
2. O HP da muralha chegar a 0 (muralha é destruída)

**Objetivos secundários**:
- Sobreviver o maior tempo possível
- Eliminar o máximo de inimigos
- Bater seus próprios records

## Controles

| Tecla | Ação |
|-------|------|
| **W** | Mover para cima |
| **A** | Mover para esquerda |
| **S** | Mover para baixo |
| **D** | Mover para direita |
| **K** | Atirar (tiro rápido - fraco) |
| **L** | Atirar (tiro lento - forte) |
| **P** | Pausar o jogo |
| **ESC** | Sair do jogo |
| **M** (Game Over) | Jogar novamente |
| **Setas ↑↓** (Menu) | Navegar menu |
| **Enter** (Menu) | Selecionar opção |

## 👹 Tipos de Inimigos

1. **Inimigo Tipo 1** (Normal)
   - HP: 2
   - Dano na muralha: 1
   - Velocidade: Média
   - Pontos: Base

2. **Inimigo Tipo 2** (Forte)
   - HP: 5  
   - Dano na muralha: 3
   - Velocidade: Lenta
   - Pontos: Médio

3. **Inimigo Tipo 3** (Boss)
   - HP: 8
   - Dano na muralha: 7
   - Velocidade: Muito lenta
   - Pontos: Alto

## Requisitos do Sistema

- Python 3.8+
- PyGame 2.5+
- cryptography (para criptografia dos records)

## 🚀 Como Executar

### Método 1: Executar com Python
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar o jogo
python Game.py
```

### Método 2: Criar executável (Windows)
```bash
# Usar o script utilitário
python utils/Criar\ exe.py
```

### Método 3: Ambiente virtual (recomendado)
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar (Linux/Mac)
source .venv/bin/activate

# Ativar (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar
python Game.py
```

## Funcionalidades Técnicas

### Sistema de Records
- Records salvos em `records.enc` (arquivo criptografado)
- Criptografia Fernet com chave fixa
- Armazena: Melhor tempo e máximo de kills
- Persistência entre sessões

### Sistema de Áudio
- Músicas diferentes para menu, jogo e pausa
- Efeitos sonoros para tiros, colisões e mortes
- Gerenciamento centralizado de volume e canais

### Sistema de Animação
- Sprites animados para todas as entidades
- Velocidade de animação ajustável
- Controle de frames por entidade

### Interface do Usuario
- Barras de vida visualizadas
- Contador de tempo e kills em tempo real
- Menu com navegação por setas
- Telas de pause 'P', game over e créditos

## Sistema de Pontuação

O jogo mantém dois records principais:

1. **Melhor Tempo**: Maior tempo de sobrevivência em segundos
2. **Máximo de Kills**: Maior número de inimigos eliminados

**Bônus**: A cada 15 inimigos mortos, você recupera 1 HP (até máximo de 4)

## Bugs Conhecidos (v2.0.0)

- A tela "Créditos" está marcada como "EM PRODUÇÃO"
- Balanceamento de dificuldade pode precisar de ajustes
- Algumas animações podem não estar perfeitamente sincronizadas

## Roadmap de Melhorias Potenciais

1. **Futuras versões**:
   - Adicionar power-ups e habilidades especiais
   - Implementar diferentes fases/ondas
   - Adicionar sistema de upgrades
   - Criar modo história com narrativa
   - Implementar multiplayer cooperativo
   - Adicionar diferentes tipos de armas

## Sobre o Desenvolvedor

Projeto pessoal desenvolvido como exercício de programação em Python com PyGame 1° semestre do curso Ciência da Computação - UFMA. A v2.0.0 representa uma refatoração completa do código original, focando em:
- Organização e legibilidade do código
- Principios de design orientado a objetos
- Separar responsabilidades em modulos
- Melhorar a manutenibilidade

## Licença

Faz o que tu quiser, irmão! assests baixados não sei de onde.

---