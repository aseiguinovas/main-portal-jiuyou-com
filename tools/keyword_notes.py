from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SAMPLE_KEYWORD = "九游"
SAMPLE_URL = "https://main-portal-jiuyou.com"


@dataclass
class KeywordNote:
    keyword: str
    url: str
    note: str
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def formatted_output(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词: {self.keyword}\n"
            f"网址  : {self.url}\n"
            f"备注  : {self.note}\n"
            f"标签  : {tag_str}\n"
            f"创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )


@dataclass
class KeywordNoteCollection:
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword in n.keyword]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        return [n for n in self.notes if tag in n.tags]

    def format_all(self) -> str:
        if not self.notes:
            return "暂无笔记。"
        parts = []
        for i, note in enumerate(self.notes, 1):
            parts.append(f"--- 笔记 {i} ---")
            parts.append(note.formatted_output())
        return "\n".join(parts)

    def summary(self) -> str:
        return f"共 {len(self.notes)} 条笔记"


def create_sample_notes() -> KeywordNoteCollection:
    collection = KeywordNoteCollection()

    note1 = KeywordNote(
        keyword=SAMPLE_KEYWORD,
        url=SAMPLE_URL,
        note="九游官方门户网站，提供丰富的游戏资讯和社区服务。",
        tags=["游戏", "门户", "资讯"],
    )
    collection.add_note(note1)

    note2 = KeywordNote(
        keyword="九游攻略",
        url=f"{SAMPLE_URL}/guides",
        note="汇集热门游戏的最新攻略和技巧分享。",
        tags=["攻略", "游戏"],
    )
    collection.add_note(note2)

    note3 = KeywordNote(
        keyword="九游社区",
        url=f"{SAMPLE_URL}/community",
        note="玩家交流、组队、讨论的互动平台。",
        tags=["社区", "社交", "游戏"],
    )
    collection.add_note(note3)

    note4 = KeywordNote(
        keyword="九游活动",
        url=f"{SAMPLE_URL}/events",
        note="定期举办各类线上活动、福利发放和赛事。",
        tags=["活动", "福利"],
    )
    collection.add_note(note4)

    return collection


def main():
    sample_collection = create_sample_notes()
    print(sample_collection.format_all())
    print(sample_collection.summary())
    print("\n筛选关键词 '九游' 的笔记：")
    for note in sample_collection.find_by_keyword("九游"):
        print(note.formatted_output())


if __name__ == "__main__":
    main()