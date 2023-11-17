from __future__ import annotations
from typing import Final as const, Optional, Any
from dataclasses import dataclass
from pydantic import BaseModel


class AuthData(BaseModel):
    """_summary_
    DXSuite API の認証情報。Auth.jsonの要素の型定義
    """
    id: int
    key: str
    domain: str
    registerDate: str
    expirationDate: str


class WorkFlowSettingResponse(BaseModel):
    """_summary\n
    ワークフロー設定取得APIのレスポンスデータ
    """
    workflowId: str
    revision: int
    applicationType: int
    ocrKindType: int 
    atypicalModelName: Any
    dataCheck: bool
    dataProcessing: bool
    outputcharCode: str


class SearchWokrFlowResponse(BaseModel):
    workflowId: str
    folderId: str
    name: str


class RegisterPOST(BaseModel):
    """
    読み取りユニット登録APIのリクエストボディ\n
    Args:\n
        files (list[str]): 読み取り対象の画像ファイルのパス\n
        unitName* (str): 読み取りユニット名\n
        departmentId* (str): 部門ID\n
    """
    files: list[str]
    unitName: Optional[str]
    departmentId: Optional[str]


class RegisterResponse(BaseModel):
    """
    読み取りユニット登録APIのレスポンスデータ
    """
    unitId: str
    unitName: str



class SearchUnitParam(BaseModel):
    """
    読み取りユニット検索APIのリクエストパラメータ
    folderId, workflowId, unitIdはカンマ区切りで複数指定可能
    """
    #指定したフォルダID内を検索する
    folderId: str
    #指定したワークフローID内を検索する
    workflowId: str
    #指定したユニットID内を検索する
    unitId: str
    #指定したユニット名内を検索する
    unitName: Optional[str] = None
    status: Optional[str] = None
    createdFrom: Optional[str] = None
    createdTo: Optional[str] = None


class SearchUnitResponse(BaseModel):
    unitId: str
    unitName: str
    status: int
    dataProcessingStatus: int
    dataCheckStatus: int
    dataCompareStatus: int
    csvDownloadStatus: int
    csvFileName: str
    folderId: str
    workflowId: str
    workflowName: str
    createdAt: str