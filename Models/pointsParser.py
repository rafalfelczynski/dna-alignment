from scoring import Scoring


def parseScoring(filePath: str):
    with open(filePath, "r") as file:
        scoring = Scoring()
        for line in file.readlines():
            key, score = line.strip().split(" ")
            if not Scoring.isAllowedKey(key):
                raise ValueError("File "+filePath+" should contain only match, mismatch and gap scorings")
            scoring[Scoring.toKey(key)] = float(score)
        return scoring


