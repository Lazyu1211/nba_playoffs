import pandas as pd
import os

PATH = "data/nba_playoffs.csv"

def get_data():
    df = pd.read_csv(PATH)
    return df

def get_total_points_pre_game():
    df = get_data()
    df["total_points_pre_game"].astype(float)
    pregame = df[df["total_points_pre_game"] > 28.00].copy()
    cond = pregame.groupby("player").sum()
    cond.sort_values(by="rank", ascending=True, inplace=True)
    cond.reset_index(inplace=True)
    return cond


def country():
    df = get_data()
    country1 = df.groupby("country")[["rank"]].count()
    country1.reset_index(inplace=True)
    return country1