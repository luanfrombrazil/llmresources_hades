# Seus subcircuitos

Blocos `.hds` do pipeline MIPS (pasta `HACKING AOC\Claude_Hades`, versões usadas por `PIPELINEPOSHAZ.hds`) e o JUMP CONTROLLER do TP02.
Cada arquivo traz: caminho para a linha `hades.models.Design`, portas com largura e posição no `.sym`, componentes internos e o `.sym` atual.

Como instanciar e como criar blocos novos: `../SUBCIRCUITOS.md`.

| Bloco | Função | Nº portas | Doc |
|---|---|---|---|
| **ALUCONTROL** | Controle da ULA: ALUOp + funct → código de operação da ULA. | 12 | [ALUCONTROL.md](ALUCONTROL.md) |
| **CONTROLLER** | Unidade de controle principal: opcode (6 bits) → barramento de controle CTL (9 bits) + BRANCH. | 3 | [CONTROLLER.md](CONTROLLER.md) |
| **CONTROLLERV1** | Versão anterior do CONTROLLER (saídas separadas). Usada por PIPELINE.hds. | 15 | [CONTROLLERV1.md](CONTROLLERV1.md) |
| **EXMEM** | Registrador de pipeline EX/MEM. | 19 | [EXMEM.md](EXMEM.md) |
| **FOWARDING UNIT** | Unidade de forwarding (adiantamento): compara registradores destino de EX/MEM e MEM/WB com rs/rt de ID/EX e gera os seletores dos Mux41. | 8 | [FOWARDING_UNIT.md](FOWARDING_UNIT.md) |
| **HAZARD UNIT** | Unidade de detecção de hazard load-use: gera PCWRITE, IFIDWRITE, NOBUBBLE e STALL. | 8 | [HAZARD_UNIT.md](HAZARD_UNIT.md) |
| **IDEX** | Registrador de pipeline ID/EX: sinais de controle, PC+4, dados lidos, imediato e campos rs/rt/rd. | 24 | [IDEX.md](IDEX.md) |
| **IDEXV1** | Versão anterior do IDEX. Usada por PIPELINE.hds. | 32 | [IDEXV1.md](IDEXV1.md) |
| **IFID** | Registrador de pipeline IF/ID: guarda PC+4 e a instrução. | 7 | [IFID.md](IFID.md) |
| **JUMP CONTROLLER** | Controle de jump do monociclo (TP02, AOC I). | 7 | [JUMP_CONTROLLER.md](JUMP_CONTROLLER.md) |
| **MEM INDEXER FIX** | Ajuste do endereço de memória (bloco auxiliar). | 2 | [MEM_INDEXER_FIX.md](MEM_INDEXER_FIX.md) |
| **MEMWB** | Registrador de pipeline MEM/WB. | 13 | [MEMWB.md](MEMWB.md) |
| **SHIFTLEFT2** | Deslocamento de 2 bits à esquerda (32 bits), para o alvo de desvio. | 2 | [SHIFTLEFT2.md](SHIFTLEFT2.md) |
| **SIGNAL EXTENDER** | Extensor de sinal 16 → 32 bits. | 2 | [SIGNAL_EXTENDER.md](SIGNAL_EXTENDER.md) |
