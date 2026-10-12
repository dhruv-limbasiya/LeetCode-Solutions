import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row = players.shape[0]
    column = players.shape[1]

    return [row, column]